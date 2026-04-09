"""Day 3 exercises: OOP, inheritance, composition, modules.

This file imports classes from day3_models.py and runs all exercises.

Run:
    python3 python-learning/day3/day3_exercises.py

JS 开发者学习提示：
1. `from x import A, B` ~= `import { A, B } from "./x"`
2. Python 用缩进表达代码块，不用 `{}`。
3. `try/except` ~= `try/catch`
4. `sorted(list, key=...)` 可类比 JS 里拷贝后 `sort(...)`
5. `if __name__ == "__main__"` ~= Node 的入口判断 `if (require.main === module)`
"""

# 具名导入：从 day3_models 模块拿到类定义。
# JS 对照：import { Circle, Rectangle, Shape, Team, User } from "./day3_models"
from day3_models import Circle, Rectangle, Shape, Team, User


# ---------------------------------------------------------------------------
# Exercise 1: User class basics
# ---------------------------------------------------------------------------
def exercise_user_basics() -> None:
    """测试 User 类的基本功能。

    JS 对照：
    - 构造实例、打印对象、调用 getter、触发异常
    """
    print("=" * 60)
    print("Exercise 1: User Class Basics")
    print("=" * 60)

    # 创建用户实例（Python 不写 new）
    # JS 对照：const alice = new User(...), const bob = new User(...)
    alice = User("Alice", "alice@gmail.com")
    bob = User("Bob", "bob@company.cn", role="editor")

    # __str__ 输出：print(obj) 会走对象的 __str__
    # JS 类比：console.log(obj.toString())
    print(f"str:  {alice}")
    print(f"str:  {bob}")

    # __repr__ 输出：开发者视角字符串（调试更常用）
    # JS 类比：你手工写 debug 展示字符串
    print(f"repr: {repr(alice)}")
    print(f"repr: {repr(bob)}")

    # @property 访问（不加括号）
    # JS getter 调用方式也一样：u.emailDomain
    print(f"Alice's email domain: {alice.email_domain}")
    print(f"Bob's email domain:   {bob.email_domain}")

    # promote 正常升级（viewer -> editor -> admin）
    print(f"\n--- Promotion ---")
    print(f"Before: {alice}")
    alice.promote()  # viewer -> editor
    print(f"After 1st promote: {alice}")
    alice.promote()  # editor -> admin
    print(f"After 2nd promote: {alice}")

    # promote 边界情况：已是 admin，继续升会抛异常
    # Python 用 try/except，JS 对照 try/catch
    try:
        alice.promote()
    except ValueError as e:
        print(f"Expected error: {e}")

    # 非法 role：构造时校验失败
    print(f"\n--- Invalid role ---")
    try:
        User("Charlie", "c@test.com", role="superadmin")
    except ValueError as e:
        print(f"Expected error: {e}")


# ---------------------------------------------------------------------------
# Exercise 2: Inheritance and Polymorphism
# ---------------------------------------------------------------------------
def exercise_shapes() -> None:
    """测试 Shape 继承体系和多态。

    多态核心：同一个接口（shape.area/describe），不同子类给出不同实现。
    """
    print(f"\n{'=' * 60}")
    print("Exercise 2: Shapes - Inheritance & Polymorphism")
    print("=" * 60)

    # 创建不同形状，类型标注为 list[Shape]
    # 含义：列表里放的是 Shape 或其子类实例
    shapes: list[Shape] = [
        Circle(5),
        Circle(1),
        Rectangle(3, 4),
        Rectangle(10, 2),
    ]

    # 多态：同一个循环处理不同类型，调用同名方法 describe()
    # JS 对照：只要对象有 describe 方法就能调（鸭子类型）
    for shape in shapes:
        print(shape.describe())

    # 面积排序（演示 key 参数 + lambda）
    # key=lambda s: s.area() 表示“按面积值排序”
    # JS 对照：const sorted = [...shapes].sort((a, b) => a.area() - b.area())
    print(f"\n--- Sorted by area (ascending) ---")
    sorted_shapes = sorted(shapes, key=lambda s: s.area())
    for shape in sorted_shapes:
        print(f"  {shape} -> area={shape.area():.2f}")

    # 基类不能直接计算面积：Shape.area() 是抽象占位实现
    print(f"\n--- Base class cannot compute area ---")
    try:
        base = Shape("Unknown")
        base.area()
    except NotImplementedError as e:
        print(f"Expected error: {e}")


# ---------------------------------------------------------------------------
# Exercise 3: Team - Composition Pattern
# ---------------------------------------------------------------------------
def exercise_team() -> None:
    """测试 Team 组合模式。

    组合（has-a）：Team 内部持有多个 User，而不是继承 User。
    """
    print(f"\n{'=' * 60}")
    print("Exercise 3: Team - Composition Pattern")
    print("=" * 60)

    # 创建团队实例
    team = Team("AI Backend")

    # 准备成员列表（Python list 对照 JS Array）
    users = [
        User("Alice", "alice@company.com", role="admin"),
        User("Bob", "bob@company.com", role="editor"),
        User("Charlie", "charlie@company.com", role="viewer"),
        User("Diana", "diana@company.com", role="viewer"),
    ]

    # 批量加入团队
    # JS 对照：for (const user of users) team.add_member(user)
    for user in users:
        team.add_member(user)

    print(f"Team: {team}")
    # len(team) 会触发 Team.__len__()
    # JS 常见写法是 team.members.length（或 getter）
    print(f"Team size: {len(team)}")

    # 按角色筛选：内部通常是列表推导式（类比 JS filter）
    print(f"\n--- Find by role ---")
    viewers = team.find_by_role("viewer")
    # [str(u) for u in viewers] 是列表推导式
    # JS 对照：viewers.map(u => String(u))
    print(f"Viewers ({len(viewers)}): {[str(u) for u in viewers]}")

    admins = team.find_by_role("admin")
    print(f"Admins ({len(admins)}): {[str(u) for u in admins]}")

    # 重复邮箱测试：应触发 ValueError
    print(f"\n--- Duplicate email rejection ---")
    try:
        duplicate = User("Alice Clone", "alice@company.com")
        team.add_member(duplicate)
    except ValueError as e:
        print(f"Expected error: {e}")


# ---------------------------------------------------------------------------
# Exercise 4: Module Import Demonstration
# ---------------------------------------------------------------------------
def exercise_module_demo() -> None:
    """演示模块导入、继承链和类型判断机制。"""
    print(f"\n{'=' * 60}")
    print("Exercise 4: Module Import")
    print("=" * 60)

    # 展示导入路径：__module__ 告诉你类定义在哪个模块
    # JS 类比：查看构造器来源文件（语言层没有完全等价内置字段）
    print(f"User class imported from: {User.__module__}")
    print(f"Circle class imported from: {Circle.__module__}")

    # 展示类的 MRO (Method Resolution Order)
    # 继承链方法查找顺序，类似你理解 prototype chain 的查找路径
    print(f"\nCircle MRO: {[cls.__name__ for cls in Circle.__mro__]}")
    print(f"Rectangle MRO: {[cls.__name__ for cls in Rectangle.__mro__]}")

    # isinstance 和 issubclass：
    # JS 对照：`instanceof`（但 Python 分成实例判断和类继承判断两个 API）
    c = Circle(3)
    print(f"\nisinstance(c, Circle): {isinstance(c, Circle)}")
    print(f"isinstance(c, Shape):  {isinstance(c, Shape)}")
    print(f"issubclass(Circle, Shape): {issubclass(Circle, Shape)}")


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # 文件作为脚本直接运行时执行；被 import 时不会执行
    # JS 对照：if (require.main === module) { ... }
    exercise_user_basics()
    exercise_shapes()
    exercise_team()
    exercise_module_demo()

    print(f"\n{'=' * 60}")
    print("All Day 3 exercises completed!")
    print("=" * 60)
