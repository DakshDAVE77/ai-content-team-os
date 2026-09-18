from pathlib import Path
import json, html
R=Path(__file__).resolve().parents[1]; O=R/'outputs'
d=json.loads((O/'current-content.json').read_text(encoding='utf-8'))
parts=['<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Content console</title><style>body{font:18px/1.5 sans-serif;max-width:900px;margin:40px auto;padding:20px}article{border:1px solid #ddd;padding:20px;margin:20px 0}p{white-space:pre-wrap}img,video{max-width:250px}button{padding:12px}</style><h1>Content console</h1><p>Select POST, then say post in your project chat.</p>']
for platform, options in d['platforms'].items():
 if platform not in ('instagram','linkedin','x'): raise ValueError('Unsupported platform')
 parts.append('<h2>'+html.escape(platform)+'</h2>')
 for variant, item in options.items():
  if variant not in ('A','B','C'): raise ValueError('Use A, B or C')
  parts.append('<article><h3>'+variant+'</h3><p>'+html.escape(item['text'])+'</p>')
  for asset in item.get('assets',[]):
   p=(R/asset).resolve()
   if not p.is_relative_to(O.resolve()) or not p.is_file(): raise ValueError('Invalid asset')
   url=html.escape(p.relative_to(O.resolve()).as_posix(),quote=True)
   parts.append(('<video controls src="'+url+'"></video>') if p.suffix.lower() in ('.mp4','.mov','.webm') else '<img alt="Selected media" src="'+url+'">')
  parts.append('<button data-platform="'+platform+'" data-variant="'+variant+'" disabled>POST</button><p role="status"></p></article>')
parts.append("""<!--LOCAL_TOKEN--><script>
const buttons=[...document.querySelectorAll('button')];
async function refresh(){const r=await fetch('/api/state');if(!r.ok)throw Error('Server unavailable');const s=await r.json();for(const b of buttons){const q=s[b.dataset.platform];b.disabled=q&&['posting','submitted','unknown','posted'].includes(q.status)&&q.pieceId===BATCH+'-'+b.dataset.platform;b.nextElementSibling.textContent=q&&q.variant===b.dataset.variant&&q.pieceId===BATCH+'-'+b.dataset.platform?(q.publishingBlocker||q.nextStep||q.status):'';}}
buttons.forEach(b=>b.onclick=async()=>{b.disabled=true;try{const r=await fetch('/api/select',{method:'POST',headers:{'Content-Type':'application/json','X-Console-Token':window.consoleToken},body:JSON.stringify({platform:b.dataset.platform,variant:b.dataset.variant})});const q=await r.json();if(!r.ok)throw Error(q.error);await refresh();}catch(e){b.nextElementSibling.textContent=e.message;b.disabled=false;}});
if(location.protocol==='file:'){document.body.insertAdjacentHTML('afterbegin','<p>Open this console through the local server at http://127.0.0.1:8767/content-console.html</p>');}else{refresh().catch(()=>{});setInterval(()=>refresh().catch(()=>{}),5000);}
</script>""".replace('BATCH',json.dumps(d['pieceId']).replace('<','\u003c')))
(O/'content-console.html').write_text(''.join(parts),encoding='utf-8')
print('Console built. Start tools/console_server.py and use localhost port 8767.')
