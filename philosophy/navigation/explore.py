#!/usr/bin/env python3
"""explore: the philosophy corpus served one neighbourhood per call, a file and what it links to, paginated, a file never twice.
Called by navigation.sh; argv: <self-path> <corpus-dir> start | <id> <file> | <id> --more"""
import json, os, re, secrets, stat, sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../tools"))
from private_temp_dir import private_temp_dir

CAP = 24_000
self_path, corpus, *args = sys.argv[1:]
session = os.environ.get("CLAUDE_CODE_SESSION_ID") or os.environ.get("OPENCODE_SESSION_ID") or "nosession"

def die(msg): print(msg, file=sys.stderr); sys.exit(1)
if not re.fullmatch(r"[a-zA-Z0-9_-]+", session): die("invalid session id")
try:
    root = private_temp_dir(os.environ["TMPDIR"]) if os.environ.get("TMPDIR") not in (None, "", "/tmp") else "/tmp"
except (ValueError, OSError) as error:
    die(str(error))
def names(): return sorted(f[:-3] for f in os.listdir(corpus) if f.endswith(".md") and not f.endswith(".work.md") and f != "README.md")
def read(n): return open(os.path.join(corpus, n + ".md"), encoding="utf-8").read()
def tags(t): m = re.search(r"^tags: *(.*)$", t, re.M); return m.group(1).strip() if m else "[]"
def thesis(t): m = re.search(r"^\*\*Thesis\.\*\* *(.*)$", t, re.M); return m.group(1).strip() if m else "—"
def links(t): return sorted({m for m in re.findall(r"φ([a-z0-9-]+)", t)})
def link(run, n): return f"→ {self_path} explore {run} {n}"
def state_path(run):
    if not re.fullmatch(r"[0-9a-f]{4}", run): die("invalid run id")
    return os.path.join(root, f"philosophy-explore-{session}-{run}.json")
def state_file(run, mode):
    path = state_path(run)
    try:
        info = os.lstat(path)
    except FileNotFoundError:
        if mode == "r": raise
        fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
        return os.fdopen(fd, mode, encoding="utf-8")
    if not stat.S_ISREG(info.st_mode) or info.st_uid != os.geteuid():
        die(f"unsafe exploration state: {path}")
    fd = os.open(path, (os.O_RDONLY if mode == "r" else os.O_WRONLY) | os.O_NOFOLLOW)
    if not stat.S_ISREG(os.fstat(fd).st_mode) or os.fstat(fd).st_uid != os.geteuid():
        os.close(fd)
        die(f"unsafe exploration state: {path}")
    if mode == "w": os.ftruncate(fd, 0)
    return os.fdopen(fd, mode, encoding="utf-8")
def load(run):
    try:
        with state_file(run, "r") as file: return json.load(file)
    except FileNotFoundError: die(f"no run {run}: start one with `{self_path} explore start`")
def save(run, st):
    with state_file(run, "w") as file: json.dump(st, file)

if not args: die("explore start | explore <id> <file> | explore <id> --more")

if args[0] == "start":
    run = secrets.token_hex(2)
    save(run, {"served": [], "queue": []})
    print(f"run {run}. Entry points, one link each:")
    for n in names():
        t = read(n)
        print(f"{n} | {tags(t)} | {thesis(t)}\n    {link(run, n)}")
    sys.exit()

run, *files = args
if len(files) > 1: die("one file per move: it is served with its neighbourhood; move to the next after reading")
st = load(run)
known = set(names())
if files == ["--more"]: files = []
unknown = [f for f in files if f not in known]
if unknown: die("no such file: " + ", ".join(unknown) + "\n(names as in the index, without .md)")
def enqueue(n):
    if n not in st["served"] and n not in st["queue"]: st["queue"].append(n)
for f in files:
    enqueue(f)
    for l in links(read(f)):
        if l in known: enqueue(l)
if not st["queue"]:
    print("nothing to serve: every file asked for was already served in this run" if files else "nothing queued"); sys.exit()

def render(served_now, queue):
    out = [f'<file name="philosophy/{n}.md">\n{read(n).rstrip()}\n</file>' for n in served_now]
    if queue: out.append(f"more ({len(queue)} queued): {self_path} explore {run} --more")
    return "\n".join(out)

# serve from the queue while the whole response, links included, fits the cap; at least one file
served_now, queue = [], list(st["queue"])
while queue:
    text = render(served_now + [queue[0]], queue[1:])
    if served_now and len(text) > CAP: break
    served_now.append(queue.pop(0)); out = text
st["served"] += served_now; st["queue"] = queue
save(run, st)
print(out)
