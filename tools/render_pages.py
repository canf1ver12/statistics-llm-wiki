"""Render PDF pages in raw/ to PNG images under raw/rendered/<source-id>/.

Usage: .venv/bin/python tools/render_pages.py "raw/統計筆記.pdf" notes 20 21 22
       .venv/bin/python tools/render_pages.py "raw/stat chap 7 ppt.pdf" ch7 50-56

Pages may be single numbers or ranges like 50-56. Rendered images are derived
files: they are regenerated on demand and ignored by git.
"""

import os
import sys

import pymupdf


def parse_pages(args: list[str]) -> list[int]:
    pages: list[int] = []
    for arg in args:
        if "-" in arg:
            start, end = arg.split("-")
            pages.extend(range(int(start), int(end) + 1))
        else:
            pages.append(int(arg))
    return pages


def main() -> None:
    path, source_id = sys.argv[1], sys.argv[2]
    out_dir = os.path.join("raw", "rendered", source_id)
    os.makedirs(out_dir, exist_ok=True)
    doc = pymupdf.open(path)
    for number in parse_pages(sys.argv[3:]):
        pixmap = doc[number - 1].get_pixmap(dpi=110)
        target = os.path.join(out_dir, f"p{number:03d}.png")
        pixmap.save(target)
        print(target)


if __name__ == "__main__":
    main()
