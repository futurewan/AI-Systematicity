"""Day 1 practice: Python basics + 3 exercises.

Run:
    python3 python-learning/day1/day1_basics.py
"""


def is_leap_year(year: int) -> bool:
    """A leap year is divisible by 4 and not by 100, unless divisible by 400."""
    # return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    return (year % 4 ==0 and year %100 != 0) or (year % 400 == 0)


def char_frequency(text: str) -> dict[str, int]:
    """Count frequency of each character in text."""
    # freq: dict[str, int] = {}
    # for ch in text:
    #     freq[ch] = freq.get(ch, 0) + 1
    # return freq

    charCount: dict[str, int] = {}
    for char in text:
        charCount[char] = charCount.get(char, 0)+1
    return charCount


def second_largest(nums: list[int]) -> int:
    """Return the second largest distinct value from nums."""
    # 1. 使用 set() 去除列表中的重复元素，得到唯一值集合
    # 2. 使用 sorted() 对唯一值进行排序，reverse=True 表示降序排列
    # 3. 结果是一个按从大到小排列的唯一值列表
    # unique = sorted(set(nums), reverse=True)
    
    # # 检查是否至少有两个不同的数字
    # # 如果唯一值数量小于2，抛出 ValueError 异常
    # if len(unique) < 2:
    #     raise ValueError("Need at least two distinct numbers.")
    
    # # 返回第二大的数（索引为1，因为列表是降序排列的）
    # # 索引0是最大的数，索引1是第二大的数
    # return unique[1]

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

    for i in range(1,5):
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


def run_exercises2() -> None:
    print("\n=== Exercise 4: Char Frequency ===")
    for index,y in enumerate([1900,2000,2030,2021]):
        print(f"{y}: {is_leap_year(y)} index={index}")

if __name__ == "__main__":
    demo_basics()
    run_exercises()
    run_exercises2()
