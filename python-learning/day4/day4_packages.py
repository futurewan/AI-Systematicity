"""Day 4: venv + pip + package structure demos.

Run:
    python3 python-learning/day4/day4_packages.py
"""

from __future__ import annotations

from dataclasses import dataclass
import platform
import sys
from typing import Iterable


@dataclass
class RequirementSpec:
    """Represents one parsed requirement line."""

    package: str
    operator: str | None
    version: str | None


def parse_requirement_line(line: str) -> RequirementSpec | None:
    """Parse a requirement line like `fastapi==0.111.0`.

    Supported operators: ==, >=, <=, >, <, ~=
    """
    line = line.strip()
    if not line or line.startswith("#"):
        return None

    operators = ["==", ">=", "<=", "~=", ">", "<"]
    for op in operators:
        if op in line:
            pkg, ver = line.split(op, 1)
            return RequirementSpec(pkg.strip(), op, ver.strip())
    return RequirementSpec(line, None, None)


def parse_requirements_lines(lines: Iterable[str]) -> list[RequirementSpec]:
    """Parse many requirement lines and skip comments/empty lines."""
    items: list[RequirementSpec] = []
    for line in lines:
        parsed = parse_requirement_line(line)
        if parsed is not None:
            items.append(parsed)
    return items


def env_info() -> dict[str, str]:
    """Collect lightweight runtime environment info."""
    return {
        "python_executable": sys.executable,
        "python_version": sys.version.split()[0],
        "platform": platform.platform(),
        "sys_prefix": sys.prefix,
        "base_prefix": sys.base_prefix,
        "in_venv": str(sys.prefix != sys.base_prefix),
    }


def suggest_venv_commands(project_root: str = ".") -> list[str]:
    """Return common commands for creating/activating a virtual environment."""
    return [
        f"python3 -m venv {project_root}/.venv",
        f"source {project_root}/.venv/bin/activate",
        "python -m pip install -U pip",
        "python -m pip install -r requirements.txt",
        "python -m pip freeze > requirements.txt",
    ]


def print_quick_demo() -> None:
    """Standalone output for quick review."""
    print("=== Day 4 Package Basics Demo ===")

    info = env_info()
    for k, v in info.items():
        print(f"{k}: {v}")

    print("\nSample requirements parsing:")
    sample_lines = [
        "fastapi==0.111.0",
        "uvicorn>=0.30.0",
        "# comment",
        "pydantic",
    ]
    for item in parse_requirements_lines(sample_lines):
        print(f"- package={item.package}, operator={item.operator}, version={item.version}")

    print("\nRecommended venv + pip commands:")
    for cmd in suggest_venv_commands("python-learning"):
        print(f"- {cmd}")


if __name__ == "__main__":
    print_quick_demo()
