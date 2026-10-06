import json, io, contextlib, traceback, types, sys
sys.path.insert(0,'.')
open('example.py','w').write('def add(a, b):\n    """This program adds two numbers and return the result"""\n    return a + b\n')
import builtins
builtins.input = lambda p="": (print(p, end=""), "1234")[1]
for ch in json.load(open('cells.json')):
    ns = {"np": __import__("numpy")}
    for i, cell in enumerate(ch["cells"]):
        code = cell["c"]
        if code.startswith("def function_name"): continue
        if "import Game" in code: continue
        buf = io.StringIO()
        try:
            with contextlib.redirect_stdout(buf), __import__("warnings").catch_warnings():
                __import__("warnings").simplefilter("ignore")
                exec(code, ns)
            got = buf.getvalue().rstrip("\n")
            status = "ERR-EXPECTED-BUT-RAN" if cell["err"] else ""
        except Exception as e:
            got = buf.getvalue() + f"{type(e).__name__}: {e}"
            status = "" if cell["err"] else "UNEXPECTED-ERROR"
        exp = (cell["o"] or "").strip()
        if status or (exp and got.strip() != exp and not cell["err"]):
            print(f"--- {ch['id']} #{i} {status}\nEXPECTED:\n{exp}\nGOT:\n{got}\n")
print("checked")
