#!/usr/bin/env python3
"""explore: the philosophy corpus served one cluster per call, paginated, a file never twice.
Called by navigation.sh; argv: <self-path> <corpus-dir> start | <id> <file>… | <id> --more"""
import json, os, re, secrets, sys

CAP = 24_000
self_path, corpus, *args = sys.argv[1:]
session = os.environ.get("CLAUDE_CODE_SESSION_ID") or os.environ.get("OPENCODE_SESSION_ID") or "nosession"

def die(msg): print(msg, file=sys.stderr); sys.exit(1)
def names(): return sorted(f[:-3] for f in os.listdir(corpus) if f.endswith(".md") and not f.endswith(".work.md") and f != "README.md")
def read(n): return open(os.path.join(corpus, n + ".md"), encoding="utf-8").read()
def tags(t): m = re.search(r"^tags: *(.*)$", t, re.M); return m.group(1).strip() if m else "[]"
def thesis(t): m = re.search(r"^\*\*Thesis\.\*\* *(.*)$", t, re.M); return m.group(1).strip() if m else "—"
def headings(t): return [h.strip() for h in re.findall(r"^## +(.*)$", t, re.M) if h.strip() != "Related"]
def links(t): return sorted({m for m in re.findall(r"\[\[philosophy/([^\]|#]+)", t)})
def link(run, n): return f"→ {self_path} explore {run} {n}"
def state_path(run): return f"/tmp/philosophy-explore-{session}-{run}.json"
def load(run):
    try: return json.load(open(state_path(run)))
    except FileNotFoundError: die(f"no run {run}: start one with `{self_path} explore start`")
def save(run, st): json.dump(st, open(state_path(run), "w"))

if not args: die("explore start | explore <id> <file>… | explore <id> --more")

if args[0] == "start":
    run = secrets.token_hex(2)
    save(run, {"served": [], "queue": []})
    print(f"run {run}. Entry points, one link each:")
    for n in names():
        t = read(n)
        print(f"{n} | {tags(t)} | {thesis(t)}\n    {link(run, n)}")
    sys.exit()

run, *files = args
st = load(run)
known = set(names())
if files == ["--more"]: files = []
unknown = [f for f in files if f not in known]
if unknown: die("no such file: " + ", ".join(unknown) + "\n(names as in the index, without .md)")
for f in files:
    if f not in st["served"] and f not in st["queue"]: st["queue"].append(f)
if not st["queue"]:
    print("nothing to serve: every file asked for was already served in this run" if files else "nothing queued"); sys.exit()

served_now, size = [], 0
while st["queue"]:
    t = read(st["queue"][0])
    if served_now and size + len(t) > CAP: break
    n = st["queue"].pop(0); st["served"].append(n); served_now.append(n); size += len(t)
    print(f'<file name="philosophy/{n}.md">\n{t.rstrip()}\n</file>')
save(run, st)

frontier = []
for n in served_now:
    for l in links(read(n)):
        if l in known and l not in st["served"] and l not in st["queue"] and l not in frontier: frontier.append(l)
if frontier:
    print("Links not yet served:")
    for n in frontier:
        t = read(n)
        print(f"  {n} {tags(t)}\n    {thesis(t)}\n    · " + "  · ".join(headings(t)) + f"\n    {link(run, n)}")
if st["queue"]:
    print(f"more ({len(st['queue'])} queued): {self_path} explore {run} --more")
