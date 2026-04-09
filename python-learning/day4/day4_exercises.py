"""Day 4 exercises: venv + pip + package structure.

Run:
    python3 python-learning/day4/day4_exercises.py
"""

from __future__ import annotations

from pathlib import Path
import sys

from day4_packages import env_info, parse_requirements_lines, suggest_venv_commands
from day4_project.app import run_app_demo


# ---------------------------------------------------------------------------
# Exercise 1: Runtime + venv basics
# ---------------------------------------------------------------------------
def exercise_env_basics() -> None:
    print("=" * 60)
    print("Exercise 1: Runtime & venv basics")
    print("=" * 60)

    info = env_info()
    for key, value in info.items():
        print(f"{key}: {value}")

    print("\nSuggested commands:")
    for cmd in suggest_venv_commands("python-learning"):
        print(f"- {cmd}")


# ---------------------------------------------------------------------------
# Exercise 2: Requirements parsing demo
# ---------------------------------------------------------------------------
def exercise_requirements_demo() -> None:
    print(f"\n{'=' * 60}")
    print("Exercise 2: requirements parsing")
    print("=" * 60)

    sample_requirements = [
        "fastapi==0.111.0",
        "uvicorn>=0.30.0",
        "httpx~=0.27.0",
        "pydantic",
        "# this is comment",
        "",
    ]

    parsed = parse_requirements_lines(sample_requirements)
    for item in parsed:
        print(f"package={item.package}, operator={item.operator}, version={item.version}")


# ---------------------------------------------------------------------------
# Exercise 3: Package import & execution
# ---------------------------------------------------------------------------
def exercise_package_imports() -> None:
    print(f"\n{'=' * 60}")
    print("Exercise 3: package imports")
    print("=" * 60)

    result = run_app_demo()
    print("run_app_demo result:")
    for key, value in result.items():
        print(f"- {key}: {value}")

    print("\nImport path check:")
    print(f"current_file: {Path(__file__).name}")
    print(f"cwd: {Path.cwd()}")
    print(f"sys.path[0]: {sys.path[0]}")


if __name__ == "__main__":
    exercise_env_basics()
    exercise_requirements_demo()
    exercise_package_imports()

    print(f"\n{'=' * 60}")
    print("All Day 4 exercises completed!")
    print("=" * 60)
