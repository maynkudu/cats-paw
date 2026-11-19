#!/usr/bin/env python3
"""Compare equal-sized RGBA images without resizing or hiding differences."""
import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('expected', type=Path)
    parser.add_argument('actual', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--threshold', type=int, default=0, help='Maximum ignored per-channel difference, 0..255')
    args = parser.parse_args()
    if not 0 <= args.threshold <= 255:
        parser.error('threshold must be between 0 and 255')
    if args.output.resolve() in {args.expected.resolve(), args.actual.resolve()}:
        parser.error('output must not overwrite either input')
    if args.output.exists():
        parser.error('output already exists; choose a new evidence path')
    try:
        from PIL import Image, ImageChops
    except ImportError:
        parser.error('Pillow is required. Use an existing document environment or an isolated virtualenv.')
    with Image.open(args.expected) as expected_file, Image.open(args.actual) as actual_file:
        expected, actual = expected_file.convert('RGBA'), actual_file.convert('RGBA')
    if expected.size != actual.size:
        parser.error(f'image dimensions differ: {expected.size} versus {actual.size}')
    difference = ImageChops.difference(expected, actual)
    changed = 0
    total_error = 0
    largest = 0
    for pixel in difference.getdata():
        maximum = max(pixel)
        changed += maximum > args.threshold
        total_error += sum(pixel)
        largest = max(largest, maximum)
    width, height = expected.size
    args.output.parent.mkdir(parents=True, exist_ok=True)
    # Make alpha differences visible rather than saving an invisible RGBA diff.
    visible = Image.new('RGB', expected.size)
    visible.putdata([tuple(max(pixel[channel], pixel[3]) for channel in range(3))
                     for pixel in difference.getdata()])
    visible.save(args.output, format='PNG')
    print(json.dumps({'width': width, 'height': height, 'threshold': args.threshold,
                      'changedPixels': changed, 'changedFraction': changed / (width * height),
                      'meanAbsoluteChannelError': total_error / (width * height * 4),
                      'maximumChannelError': largest, 'diff': str(args.output)}, indent=2))
    return 1 if changed else 0


if __name__ == '__main__':
    raise SystemExit(main())
