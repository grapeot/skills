from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(name: str) -> str:
    return (ROOT / name).read_text(encoding="utf-8")


def repo_urls_from_buttons(html: str) -> set[str]:
    return set(re.findall(r'data-url="(https://github\.com/[^"]+)"', html))


def main() -> int:
    index_en = read("index.html")
    index_zh = read("index_zh.html")
    readme_en = read("README.md")
    readme_zh = read("README_zh.md")

    checks = [
        ("English page advertises 33 skills", "33&nbsp;SKILLS" in index_en),
        ("Chinese page advertises 33 skills", "33&nbsp;个技能" in index_zh),
        ("English README links showcase", "https://grapeot.github.io/skills/" in readme_en),
        ("Chinese README links showcase", "https://grapeot.github.io/skills/index_zh.html" in readme_zh),
        ("English page has presentation_skill", "https://github.com/grapeot/presentation_skill" in index_en),
        ("Chinese page has presentation_skill", "https://github.com/grapeot/presentation_skill" in index_zh),
    ]

    en_urls = repo_urls_from_buttons(index_en)
    zh_urls = repo_urls_from_buttons(index_zh)
    checks.append(("English and Chinese pages expose the same GitHub copy URLs", en_urls == zh_urls))

    failed = [name for name, ok in checks if not ok]
    if failed:
        print("Registry checks failed:")
        for name in failed:
            print(f"- {name}")
        return 1
    print("Registry checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
