"""Day3 工具模块。"""


def format_name(name: str) -> str:
  """规范化姓名显示。"""
  return name.strip().title()


def is_valid_age(age: int) -> bool:
  """简单年龄校验：0 到 120。"""
  return 0 <= age <= 120
