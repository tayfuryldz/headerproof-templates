import json
from pathlib import Path

required = {"id", "check", "request", "matchers", "extractors", "assessment", "verification"}
manifest = json.loads(Path("templates/manifest.json").read_text())
for name in manifest["files"]:
    payload = json.loads((Path("templates") / name).read_text())
    entries = payload.get("templates", [payload])
    if not entries:
        raise SystemExit(f"{name}: no templates")
    for entry in entries:
        missing = required - entry.keys()
        if missing:
            raise SystemExit(f"{entry.get('id', name)}: missing {sorted(missing)}")
print(f"validated {sum(1 for name in manifest['files'] for _ in json.loads((Path('templates') / name).read_text()).get('templates', []))} templates")
