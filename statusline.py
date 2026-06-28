#!/usr/bin/env python3
"""Minimalist icon-driven statusline for Claude Code.
Segments, separated by " | ", no labels:  📁 folder  🔀 branch  🤖 model  🧠 NN%  🤪 compactions(>0)
🧠 % is computed against BUDGET, NOT the model context window.
"""
import sys, json, os, re, subprocess

# Windows' default stdout is cp1252, which can't encode the emoji segments.
# Force UTF-8 so 📁/🤖/🧠 render instead of crashing.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

BUDGET = 100_000  # <-- single knob: denominator for the 🧠 percentage

# On Windows, suppress the console window that subprocess would otherwise flash.
_NO_WINDOW = getattr(subprocess, "CREATE_NO_WINDOW", 0)


def compaction_count(path):
    """Count compaction events in this session's transcript.

    A real compaction is a JSONL line: type="system", subtype="compact_boundary".
    Cheap substring pre-filter, then JSON-confirm top-level — so escaped mentions
    of the word inside message content are NOT miscounted.
    """
    if not path or not os.path.isfile(path):
        return 0
    n = 0
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                if "compact_boundary" not in line:
                    continue
                try:
                    o = json.loads(line)
                except Exception:
                    continue
                if o.get("type") == "system" and o.get("subtype") == "compact_boundary":
                    n += 1
    except Exception:
        return 0
    return n


LABEL_MAX = 50  # truncate the title to this many chars, then add an ellipsis


def session_label(data):
    """The session's title, straight from Claude Code's own `ai-title`.

    Claude Code already generates a title for every session and appends it to
    the transcript JSONL as {"type":"ai-title","aiTitle":"..."} (it appears once
    there's been at least one assistant response, and is re-emitted as it
    refines). We just read the LAST such line — no hook, no Haiku call, no cost.
    Scan from the end so we grab the freshest title without parsing the whole
    file. Truncate to LABEL_MAX with an ellipsis so it never overflows the line.
    """
    path = data.get("transcript_path")
    if not path or not os.path.isfile(path):
        return ""
    title = ""
    try:
        with open(path, encoding="utf-8") as f:
            for line in reversed(f.readlines()):
                if '"ai-title"' not in line:
                    continue
                try:
                    o = json.loads(line)
                except Exception:
                    continue
                if o.get("type") == "ai-title":
                    title = (o.get("aiTitle") or "").strip()
                    break
    except Exception:
        return ""
    if len(title) > LABEL_MAX:
        title = title[:LABEL_MAX].rstrip() + "…"
    return title


def git_branch(cwd):
    """Current branch name, or "" if not in a repo or on main/master.

    Only surfaced when it's a feature branch — main/master is the assumed
    default, so showing it would be noise.
    """
    if not cwd or not os.path.isdir(cwd):
        return ""
    try:
        b = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            cwd=cwd, capture_output=True, text=True, timeout=1,
            creationflags=_NO_WINDOW,
        ).stdout.strip()
    except Exception:
        return ""
    if b in ("", "main", "master", "HEAD"):
        return ""
    return b


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        data = {}

    # 📁 folder = last segment of cwd (normpath handles \ and / separators)
    cwd = (data.get("workspace") or {}).get("current_dir") or data.get("cwd") or ""
    folder = os.path.basename(os.path.normpath(cwd)) if cwd else "?"
    folder = folder or "?"

    # 🤖 model version only — strip trailing parenthetical like "(1M context)"
    model = (data.get("model") or {}).get("display_name") or "?"
    model = re.sub(r"\s*\(.*\)\s*$", "", model).strip()

    # 🧠 context tokens against BUDGET (override the model window)
    tokens = (data.get("context_window") or {}).get("total_input_tokens")

    segs = [f"📁 {folder}"]

    # 🔀 branch — only when on a feature branch (not main/master)
    branch = git_branch(cwd)
    if branch:
        segs.append(f"🔀 {branch}")

    segs.append(f"🤖 {model}")

    if tokens is None:
        segs.append("🧠 –")
    else:
        pct = round(tokens / BUDGET * 100)
        if pct >= 110:
            color = "1;31"      # red
        elif pct >= 100:
            color = "38;5;202"  # orange-red
        elif pct >= 90:
            color = "38;5;208"  # reddish orange (halfway yellow→red)
        elif pct >= 80:
            color = "1;33"      # yellow
        else:
            color = "32"        # green
        segs.append(f"🧠 \033[{color}m{pct}%\033[0m")

    # 🤪 compaction count — omit entirely when 0
    n = compaction_count(data.get("transcript_path"))
    if n > 0:
        segs.append(f"🤪 {n}")

    out = " | ".join(segs)

    # 📌 session label on its own line under the main statusline (when ready)
    label = session_label(data)
    if label:
        out += f"\n📌 {label}"

    print(out)


main()
