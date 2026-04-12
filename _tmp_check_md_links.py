#!/usr/bin/env python3
"""
Validate local markdown references in this repo:

1. Markdown links [text](path.md) — file exists
2. Optional #fragment — heading anchor exists (GitHub-style slug from ATX ## headings)
3. Same-file links [text](#anchor) — anchor in source file
4. Backtick paths `path/to.md` — file exists
5. Prose mentions of path-like *.md (outside fences, inline code, and [...](...) links) — file exists

Limitations:
- Anchor ids are derived from ATX headings only (##/### text), using the same rules as
  common GFM slugify (may differ from GitHub in edge cases: emoji, math, HTML in headings).
- Manual <a id="..."> or heading {#custom-id} not detected.
- Very unusual punctuation in headings can diverge from GitHub; run with -v to see checks.

Exits 1 if any check fails.
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent

SKIP_DIRS = {".git", ".cursor", "node_modules", "__pycache__", ".venv", "venv"}

MD_LINK_INNER_RE = re.compile(r"\]\(\s*([^)]+?)\s*\)")
BACKTICK_MD_RE = re.compile(r"`([\w./-]+\.md)`")

# Prose: path-like token ending in .md (allows personas_jobs.md, com-b-bcw-bct/x.md)
PROSE_MD_RE = re.compile(
    r"(?<![\w/`])((?:\.\./|\./)?[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*\.md)(?![\w`/])"
)

ATX_HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")


def should_skip(path: Path) -> bool:
    return any(p in SKIP_DIRS for p in path.parts)


def iter_md_files() -> list[Path]:
    out: list[Path] = []
    for p in ROOT.rglob("*.md"):
        if should_skip(p):
            continue
        out.append(p)
    return sorted(out)


def strip_markdown_for_prose_scan(text: str) -> str:
    """Remove regions where .md tokens should not count as prose mentions."""
    # Fenced code blocks (greedy multiline)
    text = re.sub(r"^```.*?^```", " ", text, flags=re.DOTALL | re.MULTILINE)
    # Inline code
    text = re.sub(r"`[^`]+`", " ", text)
    # Markdown links and images — replace [...](...) / ![...](...) with spaces
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", " ", text)
    text = re.sub(r"\[[^\]]*\]\([^)]+\)", " ", text)
    return text


def heading_text_to_github_slug(text: str) -> str:
    """
    GitHub-style heading id from visible heading text (ATX content).
    Matches common GFM output for ASCII + unicode headings in this repo.
    """
    text = text.strip()
    # Remove optional closing ATX hashes
    text = re.sub(r"\s+#+\s*$", "", text)
    text = re.sub(r"<[^>]+>", "", text)
    # Strip simple emphasis markers
    text = re.sub(r"(\*\*|__|`)", "", text)
    text = text.lower().strip()
    # Non-word characters (except unicode letters) -> space; keep underscores as word
    text = re.sub(r"[^\w\s\u00C0-\u024F\u1E00-\u1EFF-]+", " ", text, flags=re.UNICODE)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def build_anchor_set(md_content: str) -> set[str]:
    """
    All valid fragment ids for headings in this file (GitHub duplicate rules).
    First 'foo' -> foo; second 'foo' -> foo-1; third -> foo-2
    """
    seen: dict[str, int] = defaultdict(int)
    ids: set[str] = set()
    for line in md_content.splitlines():
        m = ATX_HEADING_RE.match(line.rstrip())
        if not m:
            continue
        raw = m.group(2)
        base = heading_text_to_github_slug(raw)
        if not base:
            continue
        n = seen[base]
        seen[base] += 1
        if n == 0:
            ids.add(base)
        else:
            ids.add(f"{base}-{n}")
    return ids


# Cache anchor sets per file path (resolved)
_anchor_cache: dict[Path, set[str]] = {}


def anchors_for_file(path: Path) -> set[str]:
    path = path.resolve()
    if path in _anchor_cache:
        return _anchor_cache[path]
    text = path.read_text(encoding="utf-8", errors="replace")
    s = build_anchor_set(text)
    _anchor_cache[path] = s
    return s


def parse_link_destination(inner: str) -> tuple[str | None, str | None]:
    """
    Return (path_part, fragment) for local .md checks.
    path_part None + fragment set => same-file link (#anchor-only).
    """
    inner = inner.strip()
    if not inner:
        return None, None
    # Drop trailing "title" or 'title'
    inner = re.sub(r'\s+["\'][^"\']*["\']$', "", inner).strip()
    if inner.startswith("#"):
        frag = inner[1:].strip()
        return (None, frag if frag else None)
    if "#" not in inner:
        if not inner.endswith(".md"):
            return None, None
        return (inner, None)
    path_part, frag = inner.split("#", 1)
    path_part = path_part.strip()
    frag = frag.strip() or None
    if not path_part.endswith(".md"):
        return None, None
    return (path_part, frag)


def resolve_link_target(source_file: Path, path_part: str) -> Path | None:
    if "://" in path_part:
        return None
    if path_part.startswith("/"):
        target = (ROOT / path_part.lstrip("/")).resolve()
    else:
        target = (source_file.parent / path_part).resolve()
    try:
        target.relative_to(ROOT)
    except ValueError:
        return None
    return target


def resolve_backtick_or_prose(source_file: Path, raw: str) -> Path:
    if raw.startswith("/"):
        return (ROOT / raw.lstrip("/")).resolve()
    if raw.startswith("../") or raw.startswith("./"):
        return (source_file.parent / raw).resolve()
    return (ROOT / raw).resolve()


def main() -> int:
    import argparse

    ap = argparse.ArgumentParser(description="Validate markdown links and prose .md mentions.")
    ap.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Print each validated #fragment (file#anchor).",
    )
    args = ap.parse_args()

    md_files = iter_md_files()
    broken_file: list[tuple[str, str, str]] = []
    broken_anchor: list[tuple[str, str, str, str]] = []  # src, href, fragment, detail
    broken_ticks: list[tuple[str, str, str]] = []
    broken_prose: list[tuple[str, str, str]] = []
    tick_seen: set[tuple[str, str]] = set()

    seen_links: set[tuple[str, str, str | None]] = set()
    verbose_frags: list[str] = []
    link_count = 0
    anchor_check_count = 0

    for src in md_files:
        text = src.read_text(encoding="utf-8", errors="replace")
        src_rel = str(src.relative_to(ROOT))

        for m in MD_LINK_INNER_RE.finditer(text):
            inner = m.group(1)
            path_part, fragment = parse_link_destination(inner)
            if path_part is None and fragment is None:
                continue
            target: Path | None
            if path_part is None:
                # Same-file anchor
                target = src.resolve()
            else:
                if not path_part.endswith(".md"):
                    continue
                target = resolve_link_target(src, path_part)
                if target is None:
                    continue

            key = (src_rel, path_part or ".", fragment)
            if key in seen_links:
                continue
            seen_links.add(key)
            link_count += 1

            if not target.is_file():
                rel = target.relative_to(ROOT) if str(target).startswith(str(ROOT)) else target
                broken_file.append((src_rel, path_part or "(same file)", f"missing file: {rel}"))
                continue

            if fragment:
                anchor_check_count += 1
                ids = anchors_for_file(target)
                # GitHub allows user-content- prefix in some contexts; skip
                frag_norm = fragment.strip()
                if frag_norm not in ids:
                    # Explicit HTML ids rare in this repo; show nearby ids for debugging
                    sample = sorted(ids)[:8]
                    broken_anchor.append(
                        (
                            src_rel,
                            f"{path_part or src.name}#{frag_norm}",
                            frag_norm,
                            f"not found; example ids: {sample}",
                        )
                    )
                elif args.verbose:
                    try:
                        rel_t = target.relative_to(ROOT)
                    except ValueError:
                        rel_t = target
                    verbose_frags.append(f"{rel_t}#{frag_norm}")

        for bm in BACKTICK_MD_RE.finditer(text):
            raw = bm.group(1)
            if "://" in raw:
                continue
            tpath = resolve_backtick_or_prose(src, raw)
            try:
                tpath.relative_to(ROOT)
            except ValueError:
                continue
            if not tpath.is_file():
                tk = (src_rel, raw)
                if tk in tick_seen:
                    continue
                tick_seen.add(tk)
                rel = tpath.relative_to(ROOT) if str(tpath).startswith(str(ROOT)) else tpath
                broken_ticks.append((src_rel, raw, f"missing: {rel}"))

        prose_text = strip_markdown_for_prose_scan(text)
        prose_seen: set[str] = set()
        for pm in PROSE_MD_RE.finditer(prose_text):
            raw = pm.group(1)
            if raw.startswith("http"):
                continue
            tpath = resolve_backtick_or_prose(src, raw)
            try:
                tpath.relative_to(ROOT)
            except ValueError:
                continue
            if not tpath.is_file():
                rel = tpath.relative_to(ROOT) if str(tpath).startswith(str(ROOT)) else tpath
                key = f"{src_rel}::{raw}"
                if key in prose_seen:
                    continue
                prose_seen.add(key)
                broken_prose.append((src_rel, raw, f"missing: {rel}"))

    print(f"Scanned {len(md_files)} markdown files.")
    print(f"Checked {link_count} unique local markdown link destinations.")
    print(f"Validated {anchor_check_count} #fragment references against heading slugs.")
    if args.verbose and verbose_frags:
        print("\nAnchors OK (sample):\n  " + "\n  ".join(sorted(set(verbose_frags))[:40]))
        if len(set(verbose_frags)) > 40:
            print(f"  ... and {len(set(verbose_frags)) - 40} more")

    any_fail = bool(broken_file or broken_anchor or broken_ticks or broken_prose)

    if broken_file:
        print(f"\nBROKEN files ({len(broken_file)}):\n")
        for source, href, reason in broken_file:
            print(f"  {source}\n    {href}\n    {reason}\n")

    if broken_anchor:
        print(f"\nBROKEN anchors ({len(broken_anchor)}):\n")
        for source, href, frag, detail in broken_anchor:
            print(f"  {source}\n    link: {href}\n    fragment: {frag}\n    {detail}\n")

    if broken_ticks:
        print(f"\nBROKEN backtick paths ({len(broken_ticks)}):\n")
        for source, raw, reason in broken_ticks:
            print(f"  {source}\n    `{raw}`\n    {reason}\n")

    if broken_prose:
        print(f"\nBROKEN prose .md mentions ({len(broken_prose)}):\n")
        for source, raw, reason in broken_prose:
            print(f"  {source}\n    {raw}\n    {reason}\n")

    if not any_fail:
        print("OK — all checks passed.")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
