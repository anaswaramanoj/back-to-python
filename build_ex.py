import json, subprocess
from exercises import EX
out = {}
for cid, items in EX.items():
    lst = []
    for e in items:
        o = e.get("out")
        if not e.get("norun"):
            r = subprocess.run(["./venv/bin/python", "-c", e["sol"]], input=e.get("stdin",""), capture_output=True, text=True)
            assert r.returncode == 0, (cid, e["sol"], r.stderr)
            got = r.stdout.rstrip("\n")
            if o is None: o = got
        lst.append({"task": e["task"], "hint": e["hint"], "sol": e["sol"], "out": o})
    out[cid] = lst
js = "const EX = " + json.dumps(out, ensure_ascii=False, indent=1) + ";\n"
open("ex.js","w").write(js)
print(sum(len(v) for v in out.values()), "exercises")
for cid,v in out.items():
    for e in v: print(cid, "|", e["out"].replace("\n"," / ")[:90])
