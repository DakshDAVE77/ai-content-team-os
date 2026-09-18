# Console data
Write outputs/current-content.json using this structure. Include only completed options and existing media. Paths are project-relative. Use a distinct stable pieceId for each new batch. Optional route is text, carousel or video; assets are ordered. This example is schema only, not an instruction to publish.

```json
{"pieceId":"unique-batch-id","platforms":{"linkedin":{"A":{"text":"Final approved draft","route":"text","assets":[],"angle":"data-led","confidence":80,"confidenceLabel":"weak"}}}}
```

Supported platforms: instagram, linkedin, x. Variants: A, B, C. Run python tools/build_console.py after writing the JSON. The server saves selections under ContentEngine/state/post_request. Do not ship real selection files to other people. A new batch does not erase previous publication history.
