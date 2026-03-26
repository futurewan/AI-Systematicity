"""Day 2 exercises scaffold.
Run:
  python3 python-learning/day2/day2_exercises.py
"""


def exception_demos() -> None:
  print("=== Exception Demo ===")
  cases = [(10, 2), (5, 0), ("a", 1)]
  for a, b in cases:
    try:
      result = a / b
    except ZeroDivisionError:
      print(f"{a}/{b} -> divide by zero")
    except TypeError:
      print(f"{a}/{b} -> type error")
    else:
      print(f"{a}/{b} -> {result}")
    finally:
      pass


def comprehension_demos() -> None:
  print("\n=== Comprehension Demo ===")
  nums = [1, 2, 3, 4, 5, 6]
  squares = [x * x for x in nums]
  evens = [x for x in nums if x % 2 == 0]
  labels = ["even" if x % 2 == 0 else "odd" for x in nums]
  square_map = {x: x * x for x in range(1, 6)}

  print(f"squares={squares}")
  print(f"evens={evens}")
  print(f"labels={labels}")
  print(f"square_map={square_map}")


def char_frequency(text: str) -> dict[str, int]:
  freq: dict[str, int] = {}
  for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
  return freq


def safe_divide(a: float, b: float):
  try:
    return a / b
  except ZeroDivisionError:
    return "Error: divide by zero"


def normalize_scores(scores: list[float]) -> list[float]:
  if not scores:
    return []
  min_v = min(scores)
  max_v = max(scores)
  if max_v == min_v:
    return [0.0 for _ in scores]
  return [(x - min_v) / (max_v - min_v) for x in scores]


def top_k(nums: list[int], k: int) -> list[int]:
  if k <= 0:
    return []
  uniq = sorted(set(nums), reverse=True)
  return uniq[:k]


def run_function_tests() -> None:
  print("\n=== Function Tests ===")
  print("safe_divide:", safe_divide(10, 2), safe_divide(10, 0))
  print("normalize_scores:", normalize_scores([60, 70, 80]), normalize_scores([5, 5, 5]))
  print("top_k:", top_k([7, 2, 9, 9, 1], 2), top_k([1, 1, 1], 3))
  print("char_frequency:", char_frequency("fastapi"))


if __name__ == "__main__":
  exception_demos()
  comprehension_demos()
  run_function_tests()
