"""Screen-record a demo window using ffmpeg x11grab.

Usage:
  uv run python capture/record.py --demo "uv run python python_pyxel/pyxel_001.py" --duration 15 --keys r
  uv run python capture/record.py --demo "..." --duration 15 --keys r --position 100,50
  uv run python capture/record.py --list
"""

import argparse
import json
import os
import re
import subprocess
import sys
import time


WINDOW_TITLES = {
    'pyxel': 'Pyxel',
    'pygame': 'pygame window',
    'py5': 'Sketch',
    'turtle': 'Python Turtle Graphics',
}


def screen_size():
    result = subprocess.run(
        ['xrandr'], capture_output=True, text=True, timeout=5,
    )
    for line in result.stdout.split('\n'):
        m = re.search(r' connected primary (\d+)x(\d+)', line)
        if m:
            return int(m.group(1)), int(m.group(2))
    return 1920, 1080


def find_windows():
    result = subprocess.run(
        ['xwininfo', '-root', '-tree'],
        capture_output=True, text=True, timeout=5,
    )
    windows = []
    for line in result.stdout.split('\n'):
        # Child windows have format:
        #   WID "TITLE": (CLASS)  WxH+RelX+RelY  +AbsX+AbsY
        m = re.match(
            r'\s*(0x[0-9a-f]+)\s+"([^"]*)"\s*:\s*\(([^)]*)\)\s+'
            r'(\d+)x(\d+)([+-]\d+)([+-]\d+)\s+([+-]\d+)([+-]\d+)',
            line,
        )
        if m:
            wid, title, cls, w, h, rx, ry, ax, ay = m.groups()
            w, h, ax, ay = int(w), int(h), int(ax), int(ay)
            if w > 100 and h > 100:
                windows.append({
                    'id': wid,
                    'title': title,
                    'class': cls,
                    'width': w, 'height': h,
                    'x': ax, 'y': ay,
                    'is_content': (ax != int(rx) or ay != int(ry)),
                })
            continue

        # Frame windows have format:
        #   WID "TITLE"  WxH+X+Y
        m = re.match(r'\s*(0x[0-9a-f]+)\s+"([^"]*)"\s+(\d+)x(\d+)([+-]\d+)([+-]\d+)', line)
        if m:
            wid, title, w, h, x, y = m.groups()
            w, h, x, y = int(w), int(h), int(x), int(y)
            if w > 100 and h > 100:
                windows.append({
                    'id': wid,
                    'title': title,
                    'class': '',
                    'width': w, 'height': h,
                    'x': x, 'y': y,
                    'is_content': False,
                })

    return windows


def find_window(title=None, title_pattern=None, framework=None):
    if framework and framework.lower() in WINDOW_TITLES:
        title = WINDOW_TITLES[framework.lower()]

    windows = find_windows()

    matched = []
    if title_pattern:
        pat = re.compile(title_pattern, re.IGNORECASE)
        matched = [w for w in windows if pat.search(w['title'])]
    elif title:
        matched = [w for w in windows if title.lower() in w['title'].lower()]

    if not matched:
        return windows[0] if windows else None

    # Prefer content windows (child windows with absolute != relative position)
    content = [w for w in matched if w['is_content']]
    if content:
        return content[0]
    return matched[0]


def get_content_geometry(wid):
    """Get the content area of a window (excluding title bar/borders)."""
    result = subprocess.run(
        ['xwininfo', '-id', wid, '-stats'],
        capture_output=True, text=True, timeout=5,
    )
    if result.returncode != 0:
        raise RuntimeError(f'xwininfo failed for window {wid}')
    out = result.stdout
    x = int(re.search(r'Absolute upper-left X:\s+(\d+)', out).group(1))
    y = int(re.search(r'Absolute upper-left Y:\s+(\d+)', out).group(1))
    w = int(re.search(r'Width:\s+(\d+)', out).group(1))
    h = int(re.search(r'Height:\s+(\d+)', out).group(1))
    return x, y, w, h


def move_window(wid, x, y):
    """Move a window to a screen position using Xlib."""
    from Xlib import display
    d = display.Display()
    w = d.create_resource_object('window', int(wid, 16))
    w.configure(x=x, y=y)
    d.sync()


def send_keys(keys):
    from pynput.keyboard import Controller
    kb = Controller()
    time.sleep(0.5)
    for k in keys:
        kb.press(k)
        kb.release(k)
        time.sleep(0.3)


def record(output_path, duration=15, fps=30, region=None):
    if region is None:
        region = (0, 0) + screen_size()

    x, y, w, h = region
    # libx264 requires even dimensions
    w = w - (w % 2)
    h = h - (h % 2)
    display = os.environ.get('DISPLAY', ':0')

    cmd = [
        'ffmpeg', '-y',
        '-f', 'x11grab',
        '-video_size', f'{w}x{h}',
        '-framerate', str(fps),
        '-t', str(duration),
        '-i', f'{display}+{x},{y}',
        '-c:v', 'libx264',
        '-pix_fmt', 'yuv420p',
        '-preset', 'ultrafast',
        '-crf', '23',
        output_path,
    ]

    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc.wait(timeout=duration + 10)

    if proc.returncode != 0:
        raise RuntimeError(f'ffmpeg failed (code {proc.returncode}): {proc.stderr.read().decode(errors="replace")[:300]}')

    return output_path


def list_windows():
    for w in find_windows():
        label = '  [content]' if w['is_content'] else '  [frame]  '
        print(f'  {w["id"]} {label} "{w["title"]}"  '
              f'{w["width"]}x{w["height"]}+{w["x"]}+{w["y"]}'
              f'  class={w["class"]}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Record a demo')
    parser.add_argument('--demo', help='Command to launch the demo')
    parser.add_argument('--output', default='demo.mp4', help='Output MP4 path')
    parser.add_argument('--duration', type=int, default=15, help='Recording duration in seconds')
    parser.add_argument('--fps', type=int, default=30, help='Frames per second')
    parser.add_argument('--region', help='Capture region: X,Y,WIDTH,HEIGHT')
    parser.add_argument('--title', help='Window title to search for')
    parser.add_argument('--title-pattern', help='Regex pattern for window title')
    parser.add_argument('--framework', choices=list(WINDOW_TITLES), help='Framework default title')
    parser.add_argument('--wait', type=int, default=3, help='Seconds to wait for window')
    parser.add_argument('--keys', help='Keystrokes to send after window opens (e.g. r)')
    parser.add_argument('--position', help='Move window to X,Y (e.g. 100,50)')
    parser.add_argument('--list', action='store_true', help='List open windows and exit')

    args = parser.parse_args()

    if args.list:
        list_windows()
        sys.exit(0)

    info = {}
    region = tuple(map(int, args.region.split(','))) if args.region else None

    if not region:
        if args.demo:
            print(f'Starting demo: {args.demo}')
            subprocess.Popen(args.demo, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            time.sleep(args.wait)

        win = find_window(title=args.title, title_pattern=args.title_pattern, framework=args.framework)
        if win:
            info['window'] = win

            if args.position:
                px, py = map(int, args.position.split(','))
                # Always move the content window — this reliably repositions the whole window
                content_id = win['id'] if win['is_content'] else None
                if not content_id:
                    all_wins = find_windows()
                    content = next((w for w in all_wins
                                    if w['title'] == win['title'] and w['is_content']), None)
                    if content:
                        content_id = content['id']
                if content_id:
                    print(f'Moving to {px},{py}')
                    move_window(content_id, px, py)
                    time.sleep(1)
                    win = find_window(title=args.title, title_pattern=args.title_pattern,
                                      framework=args.framework)
                    info['window'] = win

            if win['is_content']:
                cx, cy, cw, ch = win['x'], win['y'], win['width'], win['height']
            else:
                cx, cy, cw, ch = get_content_geometry(win['id'])

            sw, sh = screen_size()

            if cx + cw > sw:
                cw = sw - cx
            if cy + ch > sh:
                ch = sh - cy

            if cw > 0 and ch > 0:
                region = (cx, cy, cw, ch)
                label = 'content' if win['is_content'] else 'frame'
                print(f'Capturing {label} area: {cx},{cy} {cw}x{ch}')

        if not region:
            print('Window not found, capturing full screen')
            region = (0, 0) + screen_size()

    if args.keys and info.get('window'):
        print(f'Sending keys: {args.keys}')
        send_keys(args.keys)

    print(f'Recording for {args.duration}s...')
    record(args.output, duration=args.duration, fps=args.fps, region=region)

    if info:
        info_path = os.path.splitext(args.output)[0] + '.json'
        with open(info_path, 'w') as f:
            json.dump(info, f)

    print(f'Saved: {args.output}')
