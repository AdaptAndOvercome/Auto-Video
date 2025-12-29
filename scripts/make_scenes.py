import sys
import json
import re

text = open(sys.argv[1], encoding="utf-8").read().strip()
sentences = re.split(r'(?<=[.!?])\s+', text)

scenes = []
current = ""

for s in sentences:
    if len(current) + len(s) < 120:
        current += " " + s
    else:
        scenes.append(current.strip())
        current = s

if current.strip():
    scenes.append(current.strip())

print(json.dumps({
    "scene_count": len(scenes),
    "scenes": scenes
}, indent=2))

