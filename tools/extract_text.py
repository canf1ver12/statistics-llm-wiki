"""Extract the text layer of a PDF in raw/ page by page.

Usage: .venv/bin/python tools/extract_text.py "raw/stat chap 7 ppt.pdf" [first_page] [last_page]

Prints "--- page N ---" before each page. Handwritten annotations and figures
are not reliable in the text layer; render those pages with render_pages.py.
"""

import sys

from pypdf import PdfReader


def main() -> None:
    path = sys.argv[1]
    reader = PdfReader(path)
    first = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    last = int(sys.argv[3]) if len(sys.argv) > 3 else len(reader.pages)
    for number in range(first, last + 1):
        text = reader.pages[number - 1].extract_text() or ""
        sys.stdout.write(f"\n--- page {number} ---\n{text}\n")


if __name__ == "__main__":
    main()
