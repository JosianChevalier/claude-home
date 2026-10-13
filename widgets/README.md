# Widgets

Not harness. These are tools for me, as a user of Claude Code: things I look at while I work. No agent loads or uses anything here.

| Widget | Where it shows | What it shows |
|---|---|---|
| `statusline.py` | under the prompt of every Claude Code session | folder, branch, model, context used, compactions |
| `quota/` | the macOS menu bar, through SwiftBar | quota used in the current window, time before reset |

## The status line also feeds the quota chip

```
Claude Code ──rate limits──▶ statusline.py ──writes──▶ quota/.statusline-snapshot.json ──read by──▶ quota/providers.py
```

Claude Code hands the rate limits to the status line at each request. The status line drops them, raw, into the quota folder, and the chip reads that file instead of calling the API. When the snapshot is stale, the chip falls back to the API.

So the two are coupled by one file and by their relative position: `statusline.py` writes into the `quota/` folder next to it.

## Wiring

- **Status line**: `statusLine.command` in `settings.json` calls `widgets/statusline.py`.
- **Quota chip**: SwiftBar's plugin folder is `widgets/quota/macos/plugin`. Details in `quota/README.md`.
