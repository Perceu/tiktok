"""Assemble intro + demo recording into final TikTok video.

Usage:
  uv run python capture/assemble.py --text "MEU TEXTO" --demo demo.mp4 --output final.mp4
  uv run python capture/assemble.py --text "MEU TEXTO" --demo demo.mp4 --crop 100,50,820,1330 --output final.mp4
"""

import argparse
import json
import os
import sys

from PIL import Image

Image.ANTIALIAS = Image.LANCZOS

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from intro import create_intro
from moviepy.editor import VideoFileClip, concatenate_videoclips


def load_info(demo_path):
    """Read sidecar .json next to the demo MP4 for auto-crop."""
    info_path = os.path.splitext(demo_path)[0] + '.json'
    if os.path.exists(info_path):
        with open(info_path) as f:
            return json.load(f)
    return {}


def assemble(
    intro_text,
    demo_path,
    output_path='final.mp4',
    outro_path=None,
    target_width=1080,
    target_height=1920,
    fps=30,
    crop=None,
):
    """Concatenate intro + demo recording + optional outro into a TikTok video."""
    if not os.path.exists(demo_path):
        raise FileNotFoundError(f'Demo video not found: {demo_path}')

    info = load_info(demo_path)
    if not crop and 'crop' in info:
        crop = tuple(info['crop'])

    print(f'Generating intro for: {intro_text}')
    intro_path = create_intro(intro_text)

    intro_clip = VideoFileClip(intro_path).resize(width=target_width)
    clips = [intro_clip]

    demo_clip = VideoFileClip(demo_path)
    if crop:
        x, y, w, h = crop
        dw, dh = demo_clip.size
        if x + w > dw:
            w = dw - x
        if y + h > dh:
            h = dh - y
        if w > 0 and h > 0:
            print(f'Cropping demo to: {x},{y} {w}x{h}')
            demo_clip = demo_clip.crop(x1=x, y1=y, x2=x + w, y2=y + h)
    demo_clip = demo_clip.resize(width=target_width, height=target_height)
    clips.append(demo_clip)

    if outro_path and os.path.exists(outro_path):
        outro_clip = VideoFileClip(outro_path).resize(width=target_width)
        clips.append(outro_clip)

    print('Concatenating clips...')
    final = concatenate_videoclips(clips, method='compose')

    print(f'Writing: {output_path}')
    final.write_videofile(
        output_path,
        fps=fps,
        codec='libx264',
        audio=False,
        threads=4,
        preset='medium',
    )

    print(f'Done: {output_path}')
    return output_path


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Assemble TikTok video from intro + demo')
    parser.add_argument('--text', required=True, help='Text for the intro animation')
    parser.add_argument('--demo', required=True, help='Path to demo recording MP4')
    parser.add_argument('--output', default='final.mp4', help='Output MP4 path')
    parser.add_argument('--outro', help='Optional outro MP4 path')
    parser.add_argument('--fps', type=int, default=30, help='Output FPS')
    parser.add_argument('--crop', help='Crop demo: X,Y,WIDTH,HEIGHT (auto-reads from sidecar .json if omitted)')
    parser.add_argument('--width', type=int, default=1080, help='Output width')
    parser.add_argument('--height', type=int, default=1920, help='Output height')

    args = parser.parse_args()
    crop = tuple(map(int, args.crop.split(','))) if args.crop else None

    assemble(
        intro_text=args.text,
        demo_path=args.demo,
        output_path=args.output,
        outro_path=args.outro,
        target_width=args.width,
        target_height=args.height,
        fps=args.fps,
        crop=crop,
    )
