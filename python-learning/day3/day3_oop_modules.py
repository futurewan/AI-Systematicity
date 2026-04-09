"""第三天练习：面向对象 + 模块化。
运行方式：
  python3 python-learning/day3/day3_oop_modules.py

给 JS 开发者的阅读提示：
1. `from utils import ...` 类似 `import { ... } from './utils'`
2. `class` / `def` 语法是缩进块，不用 `{}` 包裹
3. `__init__` 对应 JS 里的 `constructor`
4. `f"..."` 对应 JS 模板字符串 `` `...${...}` ``
5. `if __name__ == "__main__":` 对应 Node 常见入口判断 `if (require.main === module)`
"""

# 从 `utils.py` 中按名字导入函数（类似 JS 的具名导入）。
# 这里直接导入函数名，后面可以直接调用 `format_name(...)`。
from utils import format_name, is_valid_age


class User:
  """普通用户类：封装姓名、年龄、角色以及自我介绍行为。

  JS 对照：
  - `class User { ... }`：概念一致
  - Python 里实例方法必须显式写第一个参数 `self`
  - `self` 类似 JS 里的 `this`
  """

  def __init__(self, name: str, age: int, role: str = "user") -> None:
    # `name: str` / `age: int` 是类型标注（type hint），主要用于可读性和静态检查。
    # 注意：Python 默认不会在运行时强制检查类型（和 TS 不同）。
    #
    # `role: str = "user"` 是默认参数，类似 JS:
    # constructor(name, age, role = "user") {}
    #
    # 姓名统一做格式化，避免前后空格或大小写不一致。
    self.name = format_name(name)
    # `self.xxx = ...` 是给实例挂属性，等价于 JS 里的 `this.xxx = ...`
    self.age = age
    self.role = role

  def introduce(self) -> str:
    # 返回字符串：f-string 相当于 JS 模板字符串。
    return f"你好，我是{self.name}，角色是{self.role}，年龄{self.age}岁。"


class Admin(User):
  """管理员类：继承 User，并追加权限信息。

  JS 对照：
  - `class Admin(User):` 对应 `class Admin extends User`
  """

  def __init__(self, name: str, age: int, permissions: list[str]) -> None:
    # `permissions: list[str]` 类似 TS 的 `permissions: string[]`
    #
    # 通过 super() 复用父类初始化逻辑，并固定角色为 admin。
    # 对照 JS: `super(name, age, "admin")`
    super().__init__(name=name, age=age, role="admin")
    self.permissions = permissions

  def introduce(self) -> str:
    # 先复用父类介绍，再拼接管理员特有的权限描述（方法重写）。
    # 对照 JS:
    # const base = super.introduce();
    base = super().introduce()
    # `', '.join(self.permissions)` = 把数组元素用逗号拼接成字符串。
    # 对照 JS: `this.permissions.join(', ')`
    return f"{base} 我拥有权限：{', '.join(self.permissions)}。"


def demo_users() -> None:
  """演示类的实例化、继承与方法重写效果。

  JS 对照：
  - `User(" maple ", 26)` 对应 `new User(" maple ", 26)`
  - Python 实例化时不写 `new`
  """
  print("=== 类与继承演示 ===")
  user = User(" maple ", 26)
  admin = Admin("alice", 30, ["read", "write", "deploy"])
  print(user.introduce())
  print(admin.introduce())


def demo_validation() -> None:
  """演示从 utils 模块导入的年龄校验函数。"""
  print("\n=== 工具函数演示 ===")
  # Python 列表字面量和 JS 数组几乎一样。
  ages = [26, -1, 130]
  # `for age in ages:` 对应 JS 的 `for (const age of ages)`.
  for age in ages:
    print(f"age={age}, valid={is_valid_age(age)}")


def run_edge_cases() -> None:
  """演示姓名处理与年龄边界值测试。"""
  print("\n=== 边界测试 ===")
  print("姓名空格处理:", format_name("  bob  "))
  print("年龄边界(0):", is_valid_age(0))
  print("年龄边界(120):", is_valid_age(120))
  print("年龄越界(121):", is_valid_age(121))


# 入口判断：当前文件被“直接运行”时才执行下面代码。
# 如果这个文件被其他文件 import，则不会执行。
# JS 对照：`if (require.main === module) { ... }`
if __name__ == "__main__":
  demo_users()
  demo_validation()
  run_edge_cases()
