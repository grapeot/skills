from __future__ import annotations

import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PATTERNS = {
    "macOS home-directory path": re.compile(r"/Users/[A-Za-z0-9._-]+/"),
    "Linux home-directory path": re.compile(r"/home/[A-Za-z0-9._-]+/"),
    "Windows home-directory path": re.compile(r"[A-Za-z]:\\Users\\[^\\\s]+\\"),
    "secret-manager reference": re.compile(
        r"\b(?:op|vault)://[^\s`'\"]+|"
        r"arn:aws:secretsmanager:[^\s`'\"]+",
        re.IGNORECASE,
    ),
    "private IPv4 address": re.compile(
        r"\b(?:10(?:\.\d{1,3}){3}|192\.168(?:\.\d{1,3}){2}|"
        r"172\.(?:1[6-9]|2\d|3[01])(?:\.\d{1,3}){2})\b"
    ),
    "internal hostname": re.compile(
        r"\b[A-Za-z0-9.-]+\.(?:internal|corp|local|ts\.net)\b", re.IGNORECASE
    ),
    "likely access token": re.compile(
        r"\b(?:ghp_[A-Za-z0-9]{36}|github_pat_[A-Za-z0-9_]{40,}|"
        r"xox[baprs]-[A-Za-z0-9-]{20,}|AKIA[0-9A-Z]{16}|"
        r"sk-ant-[A-Za-z0-9_-]{20,}|sk-[A-Za-z0-9_-]{20,}|"
        r"sk_live_[A-Za-z0-9]{20,}|re_[A-Za-z0-9]{24,}|"
        r"AIza[0-9A-Za-z_-]{35})\b"
    ),
    "likely secret assignment": re.compile(
        r"\b(?:[A-Z0-9]+_)*(?:API_KEY|ACCESS_TOKEN|CLIENT_SECRET|PASSWORD)"
        r"\s*[:=]\s*(?:['\"][^'\"]{16,}['\"]|[^\s#'\"`]{16,})",
        re.IGNORECASE,
    ),
    "email address": re.compile(
        r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE
    ),
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
}


def tracked_text_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    paths = result.stdout.decode("utf-8").split("\0")
    return [ROOT / path for path in paths if path]


def main() -> int:
    findings: list[str] = []
    for path in tracked_text_files():
        # This checker necessarily contains the signatures it detects.
        if path.resolve() == Path(__file__).resolve():
            continue
        raw = path.read_bytes()
        if b"\0" in raw:
            continue
        text = raw.decode("utf-8", errors="replace")
        relative = path.relative_to(ROOT)
        for line_number, line in enumerate(text.splitlines(), start=1):
            for label, pattern in PATTERNS.items():
                if pattern.search(line):
                    findings.append(f"{relative}:{line_number}: {label}")

    if findings:
        print("Public-content checks failed:")
        for finding in findings:
            print(f"- {finding}")
        print("Review each finding. Remove private content rather than allowlisting it by default.")
        return 1

    print("Public-content checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
