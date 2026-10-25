"""Synchronize derived counters in the hand-authored showcase pages.

Add or edit skill rows in index.html and index_zh.html as usual, then run:
    python scripts/sync_registry.py

The script renumbers all rows in document order, updates each group's counter,
and updates the advertised total. Entry content remains hand-authored.
"""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ROW_NUMBER_RE = re.compile(
    r'(<span style="font:600 12px \'IBM Plex Mono\',monospace; '
    r'color:#b9c0cb; padding-top:3px;">)\d+(</span>)'
)
GROUP_BLOCK_RE = re.compile(
    r'<div class="sk-group" data-group="[^"]+">.*?(?=<div class="sk-group"|</main>)',
    re.DOTALL,
)
GROUP_COUNT_RE = re.compile(
    r'(<span style="font:600 11px \'IBM Plex Mono\',monospace; '
    r'color:#aeb6c1;">)\d+(</span>)'
)
HEADER_COUNT_RES = {
    "index.html": re.compile(r"(THE&nbsp;REGISTRY &nbsp;·&nbsp; )\d+(&nbsp;SKILLS)"),
    "index_zh.html": re.compile(r"(收录 )\d+(&nbsp;个技能)"),
}


def replace_once(pattern: re.Pattern[str], replacement, text: str, label: str) -> str:
    updated, count = pattern.subn(replacement, text)
    if count != 1:
        raise ValueError(f"Expected exactly one {label}, found {count}")
    return updated


def sync_page(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    row_count = text.count('class="sk-row"')
    if row_count == 0:
        raise ValueError(f"No skill rows found in {path.name}")

    group_counts: list[tuple[str, int]] = []

    def sync_group(match: re.Match[str]) -> str:
        block = match.group(0)
        name = re.search(r'data-group="([^"]+)"', block).group(1)
        count = block.count('class="sk-row"')
        group_counts.append((name, count))
        return replace_once(
            GROUP_COUNT_RE,
            lambda m: f"{m.group(1)}{count:02d}{m.group(2)}",
            block,
            f"counter for group {name} in {path.name}",
        )

    text = GROUP_BLOCK_RE.sub(sync_group, text)
    if sum(count for _, count in group_counts) != row_count:
        raise ValueError(f"Group rows do not cover all skill rows in {path.name}")

    sequence = iter(range(1, row_count + 1))
    text = replace_once(
        HEADER_COUNT_RES[path.name],
        lambda m: f"{m.group(1)}{row_count}{m.group(2)}",
        text,
        f"advertised total in {path.name}",
    )
    text, numbered = ROW_NUMBER_RE.subn(
        lambda m: f"{m.group(1)}{next(sequence)}{m.group(2)}", text
    )
    if numbered != row_count:
        raise ValueError(f"Expected {row_count} row numbers in {path.name}, found {numbered}")

    if text != path.read_text(encoding="utf-8"):
        path.write_text(text, encoding="utf-8")
    groups = ", ".join(f"{name}={count}" for name, count in group_counts)
    return f"{path.name}: {row_count} skills ({groups})"


def main() -> int:
    for name in ("index.html", "index_zh.html"):
        print(sync_page(ROOT / name))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
