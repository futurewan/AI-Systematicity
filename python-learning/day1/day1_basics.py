"""Day 1 practice: Python basics + 3 exercises.

Run:
    python3 python-learning/day1/day1_basics.py
"""


def is_leap_year(year: int) -> bool:
    """A leap year is divisible by 4 and not by 100, unless divisible by 400."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def char_frequency(text: str) -> dict[str, int]:
    """Count frequency of each character in text."""
    freq: dict[str, int] = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    return freq


def second_largest(nums: list[int]) -> int:
    """Return the second largest distinct value from nums."""
    unique = sorted(set(nums), reverse=True)
    if len(unique) < 2:
        raise ValueError("Need at least two distinct numbers.")
    return unique[1]


def demo_basics() -> None:
    # variables and basic data structures
    name = "Maple"
    score = 88
    is_active = True
    skills = ["python", "fastapi", "rag"]
    profile = {"name": name, "score": score, "active": is_active}

    name2 = "maple2"
    score2 = 99
    is_active2 = False
    skills2 = ["python2","fastapi2","tag2"]
    profile2 = {"name":name2,"score":score2,"active":is_active2}


    print("=== Basic Demo ===")
    print(f"name={name}, score={score}, active={is_active}")
    print(f"skills={skills}")
    print(f"profile={profile}")

    print("\n===Basic Demo2 ===")
    print(f"name={name2}, score={score2}, active={is_active2}")
    print(f"skills={skills2}")

    # condition + loop
    print("\n=== Loop Demo ===")
    for i in range(1, 6):
        label = "even" if i % 2 == 0 else "odd"
        print(f"{i} is {label}")


def run_exercises() -> None:
    print("\n=== Exercise 1: Leap Year ===")
    for y in [1900, 2000, 2024, 2025]:
        print(f"{y}: {is_leap_year(y)}")

    print("\n=== Exercise 2: Char Frequency ===")
    text = "fastapi"
    print(f"text={text}, freq={char_frequency(text)}")

    print("\n=== Exercise 3: Second Largest ===")
    nums = [7, 2, 9, 9, 5, 3]
    print(f"nums={nums}, second_largest={second_largest(nums)}")


if __name__ == "__main__":
    demo_basics()
    run_exercises()
