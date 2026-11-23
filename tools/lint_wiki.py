"""Mechanical lint checks for the wiki (the automatable part of node N4).

Usage: .venv/bin/python tools/lint_wiki.py

Checks:
  links     relative Markdown links that point to missing files
  orphans   concept/source pages with no inbound link (index and log don't count)
  index     wiki pages not listed in index.md
  citation  concept-page lines with content but no source citation or 補充說明 marker
  style     Chinese full stop, emoji, and Mainland-Chinese terms
            (also applied to AGENTS.md, CLAUDE.md, README.md and docs/*.md)

Judgement checks (page numbers, formula correctness, contradictions) are done
by reading, not by this script. Exit code is 1 when any check fails.
"""

import os
import re
import sys

WIKI = "wiki"
LINK_RE = re.compile(r"\]\(([^)#\s]+)(?:#[^)]*)?\)")
EMOJI_RE = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐✅]")
MAINLAND_TERMS = [
    "數據", "默認", "信息", "質量", "視頻", "軟件", "用戶", "創建", "優化",
    "文件夾", "代碼", "變量", "內存", "屏幕", "接口", "登錄", "服務器", "網絡",
]
# "函數" is intentionally absent: Taiwan math usage (機率密度函數) is correct;
# only the programming sense should be 函式.
# Sections in concept pages whose lines are navigation, not claims
NO_CITATION_SECTIONS = {"相關概念", "來源"}


def wiki_pages() -> list[str]:
    pages = []
    for root, _, files in os.walk(WIKI):
        for name in files:
            if name.endswith(".md"):
                pages.append(os.path.normpath(os.path.join(root, name)))
    return sorted(pages)


def strip_code(text: str) -> str:
    """Drop fenced code blocks so examples in them are not linted."""
    return re.sub(r"```.*?```", "", text, flags=re.S)


def check_links(pages: list[str]) -> tuple[list[str], dict[str, set[str]]]:
    problems = []
    inbound: dict[str, set[str]] = {p: set() for p in pages}
    for page in pages:
        text = strip_code(open(page, encoding="utf-8").read())
        for target in LINK_RE.findall(text):
            if target.startswith(("http://", "https://")):
                continue
            resolved = os.path.normpath(os.path.join(os.path.dirname(page), target))
            if not os.path.exists(resolved):
                problems.append(f"{page}: broken link -> {target}")
            elif resolved in inbound and resolved != page:
                inbound[resolved].add(page)
    return problems, inbound


def check_orphans(pages: list[str], inbound: dict[str, set[str]]) -> list[str]:
    ignored = {os.path.join(WIKI, "index.md"), os.path.join(WIKI, "log.md")}
    problems = []
    for page in pages:
        if not page.startswith((os.path.join(WIKI, "concepts"), os.path.join(WIKI, "sources"))):
            continue
        if not inbound[page] - ignored:
            problems.append(f"{page}: orphan (only index/log link here)")
    return problems


def check_index(pages: list[str]) -> list[str]:
    index_path = os.path.join(WIKI, "index.md")
    index_text = open(index_path, encoding="utf-8").read()
    problems = []
    for page in pages:
        rel = os.path.relpath(page, WIKI)
        if rel in ("index.md", "log.md"):
            continue
        if f"]({rel})" not in index_text:
            problems.append(f"{page}: not listed in index.md")
    return problems


def check_citations(pages: list[str]) -> list[str]:
    problems = []
    for page in pages:
        if not page.startswith(os.path.join(WIKI, "concepts")):
            continue
        section = ""
        lines = open(page, encoding="utf-8").read().splitlines()
        start = 0
        if lines and lines[0].strip() == "---":
            start = lines.index("---", 1) + 1  # skip YAML frontmatter
        in_math = False
        for number, line in enumerate(lines[start:], start + 1):
            stripped = line.strip()
            if not stripped:
                continue
            # Display math is covered by the citation on the line introducing it
            if stripped == "$$":
                in_math = not in_math
                continue
            if in_math or (stripped.startswith("$$") and stripped.endswith("$$")):
                continue
            if stripped.startswith("#"):
                # Text under the H1 title is a page description, not a claim
                is_title = stripped.startswith("# ")
                section = "" if is_title else stripped.lstrip("#").strip()
                continue
            if not section:
                continue
            if section in NO_CITATION_SECTIONS or stripped.startswith("|---"):
                continue
            following = lines[number].strip() if number < len(lines) else ""
            if stripped.startswith("|") and following.startswith("|---"):
                continue  # table header row
            if "](../sources/" in stripped or "補充說明" in stripped:
                continue
            if section.startswith("例子") and stripped.startswith("|"):
                continue  # rows of an example table cited in the line above it
            problems.append(f"{page}:{number}: no citation [{section}] {stripped[:50]}")
    return problems


def check_style(pages: list[str]) -> list[str]:
    problems = []
    for page in pages:
        text = open(page, encoding="utf-8").read()
        for number, line in enumerate(text.splitlines(), 1):
            if "。" in line and "「。」" not in line:  # the style rule itself quotes 。
                problems.append(f"{page}:{number}: Chinese full stop")
            if EMOJI_RE.search(line):
                problems.append(f"{page}:{number}: emoji")
            # log.md quotes past mistakes verbatim, so only check its punctuation
            for term in ([] if page.endswith("log.md") else MAINLAND_TERMS):
                if term in line:
                    problems.append(f"{page}:{number}: Mainland term '{term}'")
    return problems


def extra_docs() -> list[str]:
    """Project docs outside wiki/ that follow the same writing style (style check only)."""
    docs = ["AGENTS.md", "CLAUDE.md", "README.md"]
    if os.path.isdir("docs"):
        docs += [os.path.join("docs", f) for f in sorted(os.listdir("docs")) if f.endswith(".md")]
    return [d for d in docs if os.path.exists(d)]


def main() -> None:
    pages = wiki_pages()
    link_problems, inbound = check_links(pages)
    results = {
        "links": link_problems,
        "orphans": check_orphans(pages, inbound),
        "index": check_index(pages),
        "citation": check_citations(pages),
        "style": check_style(pages + extra_docs()),
    }
    failed = False
    for name, problems in results.items():
        status = "FAIL" if problems else "PASS"
        print(f"[{status}] {name} ({len(problems)})")
        for problem in problems:
            print(f"    {problem}")
        failed = failed or bool(problems)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
