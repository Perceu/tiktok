# TikTok demos — repo guide

Standalone Python demo scripts shown on TikTok
[@perceubertoletti](https://www.tiktok.com/@perceubertoletti).

Managed with **uv**. Install deps: `uv sync`.

## Structure

| Directory | Library | Notes |
|-----------|---------|-------|
| `python_turtle/` | `turtle` (stdlib) | Largest (39 files). Uses `functions.py` helpers. |
| `python_pyxel/` | `pyxel` | 12 files. Retro game engine. Handles its own window. |
| `python_py5/` | `py5` | 8 files. Processing-inspired. Requires X server. |
| `python_pygame/` | `pygame` | 7 files + `common/` helpers (firework, starfield). Requires X server. |
| `python_ncurses/` | `curses` (stdlib) | 4 files + `desenhos/` ASCII art. |
| `intro.py` | Pillow + moviepy | Generates intro MP4. Exposes `create_intro(text)` for imports. |
| `capture/` | ffmpeg + moviepy | Screen recording & video assembly pipeline. |
| `statics/` | — | Shared assets: `fonts/montserrat.ttf`, `logos/*.png`, `helpers.py` |

## Commands

```bash
uv sync                          # Install all deps
uv run python intro.py "TEXTO"   # Generate intro MP4 (CLI)
uv run python python_turtle/turtle_001.py  # Run any demo
```

### Capture pipeline

```bash
# Record a demo for 15s (auto-detect window, send 'r' to start)
uv run python capture/record.py \
  --demo "uv run python python_pyxel/pyxel_001.py" \
  --duration 15 \
  --keys r

# List open windows to find the right one
uv run python capture/record.py --list

# Position the window at a specific screen location
uv run python capture/record.py \
  --demo "..." --duration 15 --keys r \
  --position 100,50

# Specify region manually (X,Y,WIDTH,HEIGHT)
uv run python capture/record.py --region 100,50,720,1280 --duration 15

# Assemble intro + recording into final video
uv run python capture/assemble.py --text "MEU TEXTO" --demo demo.mp4 --output final.mp4

# Full workflow example (positioned at top of screen to avoid clipping):
uv run python capture/record.py \
  --demo "uv run python python_pygame/pygame_006.py" \
  --framework pygame \
  --duration 12 \
  --keys r \
  --position 100,0 \
  --output demo.mp4 \
&& uv run python capture/assemble.py --text "TÍTULO" --demo demo.mp4 --output tiktok.mp4
```

## Quirks

- **No tests, no CI, no linter/formatter** — all standalone demos.
- **All demos now use 576×1024** (9:16 portrait, fits on 1080p screen for clean window capture).
- **Most demos need `r` key to start** — pass `--keys r` to `record.py` to auto-press it.
- **X server required** for GUI demos (pygame, py5, turtle). pyxel handles its own window.
- **`build/`** is gitignored — used by `intro.py` for frame cache.
- **`*.mp4`** output is gitignored.
- **All filenames/comments in Portuguese (BR)**.
- **Window titles** (for capture): pyxel→`"Pyxel"`, pygame→`"pygame window"`, py5→`"Sketch"`, turtle→`"Python Turtle Graphics"`.
- **`Image.ANTIALIAS` patch**: `assemble.py` sets `Image.ANTIALIAS = Image.LANCZOS` for Pillow 11 compat.
- **Content-area detection**: `record.py` parses `xwininfo -root -tree` to find the content sub-window (child with class matching the app, not `mutter-x11-frames`). This automatically excludes title bars and window decorations from the capture region.
- **Window positioning** (`--position X,Y`): uses `python-xlib` to move the content window, then re-scans `-root -tree` to get the new content position. GNOME CSD may add offset (typically ~37px top, 0px left).
- **libx264 requires even dimensions**: `record.py` auto-rounds width/height down to even numbers to avoid encoder errors.
- **`--framework` flag** sets default title & wait times per framework.
