"""Local content selection console. Never publishes to a social service."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import json, secrets, datetime, os, threading

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'outputs'
STATE = ROOT / 'ContentEngine/state/post_request'
PORT = 8767
TOKEN = secrets.token_urlsafe(32)
LOCK = threading.Lock()

class Handler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(OUTPUT), **kwargs)

    def reply(self, code, data):
        body = json.dumps(data).encode()
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.headers.get('Host') != f'127.0.0.1:{PORT}':
            return self.reply(403, {'error': 'Local access only'})
        if self.path == '/api/state':
            result = {}
            with LOCK:
                for platform in ('instagram', 'linkedin', 'x'):
                    path = STATE / f'{platform}.json'
                    if path.exists(): result[platform] = json.loads(path.read_text(encoding='utf-8'))
            return self.reply(200, result)
        if self.path in ('/', '/content-console.html'):
            body = (OUTPUT / 'content-console.html').read_text(encoding='utf-8')
            body = body.replace('<!--LOCAL_TOKEN-->', '<script>window.consoleToken=' + json.dumps(TOKEN) + '</script>')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Cache-Control', 'no-store')
            self.end_headers()
            self.wfile.write(body.encode('utf-8'))
            return
        super().do_GET()

    def do_POST(self):
        if (self.path != '/api/select' or self.headers.get('Host') != f'127.0.0.1:{PORT}'
            or self.headers.get('Origin') != f'http://127.0.0.1:{PORT}'
            or self.headers.get('X-Console-Token') != TOKEN):
            return self.reply(403, {'error': 'Open the local console to select an option.'})
        try:
            size = int(self.headers.get('Content-Length', 0))
            if not 0 < size < 1024: raise ValueError()
            request = json.loads(self.rfile.read(size))
            platform, variant = request['platform'], request['variant']
            if platform not in ('instagram','linkedin','x'): raise ValueError()
            if variant not in ('A', 'B', 'C'): raise ValueError()
        except (ValueError, KeyError, TypeError):
            return self.reply(400, {'error': 'Invalid selection'})
        with LOCK:
            path = STATE / f'{platform}.json'
            old = json.loads(path.read_text(encoding='utf-8')) if path.exists() else {}
            batch = json.loads((OUTPUT / 'current-content.json').read_text(encoding='utf-8'))
            piece_id = batch['pieceId'] + '-' + platform
            if old.get('postizId') or old.get('status') in ('posting', 'submitted', 'unknown') or (old.get('status') == 'posted' and old.get('pieceId') == piece_id):
                return self.reply(409, {'error': 'An existing publication must be reconciled before changing the selection.'})
            try:
                data = batch['platforms'][platform][variant]
                assets = data.get('assets', [])
                for asset in assets:
                    resolved = (ROOT / asset).resolve()
                    if not resolved.is_relative_to(OUTPUT.resolve()) or not resolved.is_file():
                        return self.reply(409, {'error': 'Media must exist inside outputs.'})
                if not data['text'].strip(): raise ValueError()
            except (KeyError, TypeError, ValueError):
                return self.reply(400, {'error': 'This option is unavailable or incomplete.'})
            record = dict(pieceId=piece_id, variant=variant, text=data['text'],
                angle=data.get('angle', variant), confidence=data.get('confidence'),
                confidenceLabel=data.get('confidenceLabel'),
                requestedAt=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                requestedBy='local console user (identity not authenticated)',
                provenance='Explicit POST click for this exact content',
                route=data.get('route', 'text'), assets=assets, status='queued',
                publicationAuthorized=True, dispatch='chat',
                nextStep='Say post in this project chat to publish selected platforms.')
            STATE.mkdir(parents=True, exist_ok=True)
            if old:
                archive = STATE / 'history'; archive.mkdir(exist_ok=True)
                (archive / f'{platform}-{secrets.token_hex(8)}.json').write_text(json.dumps(old,ensure_ascii=False,indent=2),encoding='utf-8')
            temporary = path.with_suffix('.tmp')
            temporary.write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
            os.replace(temporary, path)
        self.reply(200, record)

if __name__ == '__main__':
    ThreadingHTTPServer(('127.0.0.1', PORT), Handler).serve_forever()
