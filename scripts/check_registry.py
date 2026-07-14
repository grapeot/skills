from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AGY_EN_URL = "https://github.com/grapeot/context-infrastructure-en/blob/main/rules/skills/antigravity_cli.md"
AGY_ZH_URL = "https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/antigravity_cli.md"
REGISTRY_LIFECYCLE_URL = "https://github.com/grapeot/skills/blob/master/skills/skill_registry_lifecycle.md"


def read(name: str) -> str:
    return (ROOT / name).read_text(encoding="utf-8")


def repo_urls_from_buttons(html: str) -> set[str]:
    return set(re.findall(r'data-url="(https://github\.com/[^"]+)"', html))


def canonical_skill_url(url: str) -> str:
    """Treat localized context-infrastructure files as the same skill."""
    return AGY_ZH_URL if url == AGY_EN_URL else url


def has_one_copy_and_link(html: str, url: str) -> bool:
    return html.count(f'data-url="{url}"') == 1 and html.count(f'href="{url}"') == 1


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
    agents = read("AGENTS.md")

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
            ("English page has one copy button and direct link for the English Antigravity skill",
             has_one_copy_and_link(index_en, AGY_EN_URL)),
            ("Chinese page has one copy button and direct link for the Chinese Antigravity skill",
             has_one_copy_and_link(index_zh, AGY_ZH_URL)),
            ("English README links the registry lifecycle skill",
             "skills/skill_registry_lifecycle.md" in readme_en),
            ("Chinese README links the registry lifecycle skill",
             "skills/skill_registry_lifecycle.md" in readme_zh),
            ("Registry lifecycle skill exists",
             (ROOT / "skills/skill_registry_lifecycle.md").is_file()),
            ("Agent instructions require the registry lifecycle skill",
             "skills/skill_registry_lifecycle.md" in agents),
            ("Agent instructions disable auto-merge",
             "Do not enable auto-merge" in agents),
            ("English page has one copy button and direct link for the registry lifecycle skill",
             has_one_copy_and_link(index_en, REGISTRY_LIFECYCLE_URL)),
            ("Chinese page has one copy button and direct link for the registry lifecycle skill",
             has_one_copy_and_link(index_zh, REGISTRY_LIFECYCLE_URL)),
            ("English and Chinese pages expose the same localized GitHub skills",
             {canonical_skill_url(url) for url in repo_urls_from_buttons(index_en)}
             == {canonical_skill_url(url) for url in repo_urls_from_buttons(index_zh)}),
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
