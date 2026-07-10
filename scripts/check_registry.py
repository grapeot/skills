from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(name: str) -> str:
    return (ROOT / name).read_text(encoding="utf-8")


def repo_urls_from_buttons(html: str) -> set[str]:
    return set(re.findall(r'data-url="(https://github\.com/[^"]+)"', html))


def advertised_count(html: str, *, label: str) -> int | None:
    """Extract the skill count advertised in the page header.

    Matches both the English form ("N SKILLS") and the Chinese form
    ("N 个技能"), tolerating the &nbsp; entities used in the markup.
    """
    m = re.search(r"(\d+)(?:&nbsp;)?\s*" + re.escape(label), html)
    return int(m.group(1)) if m else None


def group_counts(html: str) -> list[int]:
    """Return the per-group counts shown next to each group heading."""
    return [int(x) for x in re.findall(
        r'color:#aeb6c1;">(\d+)</span>', html)]


def sequence_numbers(html: str) -> list[int]:
    """Return the per-row sequence numbers in document order."""
    return [int(x) for x in re.findall(
        r'color:#b9c0cb; padding-top:3px;">(\d+)</span>', html)]


def check_continuity(nums: list[int]) -> str | None:
    """Return an error message if `nums` is not a 1-based contiguous run."""
    if not nums:
        return "no skill sequence numbers found"
    expected = list(range(1, len(nums) + 1))
    if nums != expected:
        return f"sequence numbers are not contiguous from 1: got {nums}"
    return None


def main() -> int:
    index_en = read("index.html")
    index_zh = read("index_zh.html")
    readme_en = read("README.md")
    readme_zh = read("README_zh.md")

    failed: list[str] = []

    for label, html in (("EN", index_en), ("ZH", index_zh)):
        advertised = advertised_count(html, label="SKILLS" if label == "EN" else "个技能")
        rows = len(re.findall(r'class="sk-row"', html))
        if advertised is None:
            failed.append(f"{label} page does not advertise a skill count")
        elif advertised != rows:
            failed.append(
                f"{label} page advertises {advertised} skills but has {rows} rows"
            )

        nums = sequence_numbers(html)
        err = check_continuity(nums)
        if err:
            failed.append(f"{label} page {err}")
        elif len(nums) != rows:
            failed.append(
                f"{label} page has {rows} rows but {len(nums)} sequence numbers"
            )

        gc = group_counts(html)
        if sum(gc) != rows:
            failed.append(
                f"{label} page group counters sum to {sum(gc)} but there are {rows} rows"
            )

    failed.extend([
        name for name, ok in [
            ("English README links showcase", "https://grapeot.github.io/skills/" in readme_en),
            ("Chinese README links showcase", "https://grapeot.github.io/skills/index_zh.html" in readme_zh),
            ("English page has presentation_skill", "https://github.com/grapeot/presentation_skill" in index_en),
            ("Chinese page has presentation_skill", "https://github.com/grapeot/presentation_skill" in index_zh),
            ("English and Chinese pages expose the same GitHub copy URLs",
             repo_urls_from_buttons(index_en) == repo_urls_from_buttons(index_zh)),
        ] if not ok
    ])

    if failed:
        print("Registry checks failed:")
        for name in failed:
            print(f"- {name}")
        return 1
    print("Registry checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())