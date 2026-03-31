"""Day 3 exercises: OOP, inheritance, composition, modules.

This file imports classes from day3_models.py and runs all exercises.

Run:
    python3 python-learning/day3/day3_exercises.py
"""

from day3_models import Circle, Rectangle, Shape, Team, User


# ---------------------------------------------------------------------------
# Exercise 1: User class basics
# ---------------------------------------------------------------------------
def exercise_user_basics() -> None:
    """测试 User 类的基本功能。"""
    print("=" * 60)
    print("Exercise 1: User Class Basics")
    print("=" * 60)

    # 创建用户实例
    alice = User("Alice", "alice@gmail.com")
    bob = User("Bob", "bob@company.cn", role="editor")

    # __str__ 输出
    print(f"str:  {alice}")
    print(f"str:  {bob}")

    # __repr__ 输出
    print(f"repr: {repr(alice)}")
    print(f"repr: {repr(bob)}")

    # @property 访问（不加括号）
    print(f"Alice's email domain: {alice.email_domain}")
    print(f"Bob's email domain:   {bob.email_domain}")

    # promote 正常升级
    print(f"\n--- Promotion ---")
    print(f"Before: {alice}")
    alice.promote()  # viewer -> editor
    print(f"After 1st promote: {alice}")
    alice.promote()  # editor -> admin
    print(f"After 2nd promote: {alice}")

    # promote 边界情况：已是 admin
    try:
        alice.promote()
    except ValueError as e:
        print(f"Expected error: {e}")

    # 非法 role
    print(f"\n--- Invalid role ---")
    try:
        bad_user = User("Charlie", "c@test.com", role="superadmin")
    except ValueError as e:
        print(f"Expected error: {e}")


# ---------------------------------------------------------------------------
# Exercise 2: Inheritance and Polymorphism
# ---------------------------------------------------------------------------
def exercise_shapes() -> None:
    """测试 Shape 继承体系和多态。"""
    print(f"\n{'=' * 60}")
    print("Exercise 2: Shapes - Inheritance & Polymorphism")
    print("=" * 60)

    # 创建不同形状
    shapes: list[Shape] = [
        Circle(5),
        Circle(1),
        Rectangle(3, 4),
        Rectangle(10, 2),
    ]

    # 多态：同一个循环处理不同类型
    for shape in shapes:
        print(shape.describe())

    # 面积排序（演示 key 参数 + lambda）
    print(f"\n--- Sorted by area (ascending) ---")
    sorted_shapes = sorted(shapes, key=lambda s: s.area())
    for shape in sorted_shapes:
        print(f"  {shape} -> area={shape.area():.2f}")

    # 基类不能直接使用
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
    """测试 Team 组合模式。"""
    print(f"\n{'=' * 60}")
    print("Exercise 3: Team - Composition Pattern")
    print("=" * 60)

    # 创建团队
    team = Team("AI Backend")

    # 添加成员
    users = [
        User("Alice", "alice@company.com", role="admin"),
        User("Bob", "bob@company.com", role="editor"),
        User("Charlie", "charlie@company.com", role="viewer"),
        User("Diana", "diana@company.com", role="viewer"),
    ]

    for user in users:
        team.add_member(user)

    print(f"Team: {team}")
    print(f"Team size: {len(team)}")

    # 按角色筛选
    print(f"\n--- Find by role ---")
    viewers = team.find_by_role("viewer")
    print(f"Viewers ({len(viewers)}): {[str(u) for u in viewers]}")

    admins = team.find_by_role("admin")
    print(f"Admins ({len(admins)}): {[str(u) for u in admins]}")

    # 重复邮箱测试
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
    """演示模块导入机制。"""
    print(f"\n{'=' * 60}")
    print("Exercise 4: Module Import")
    print("=" * 60)

    # 展示导入路径
    print(f"User class imported from: {User.__module__}")
    print(f"Circle class imported from: {Circle.__module__}")

    # 展示类的 MRO (Method Resolution Order)
    print(f"\nCircle MRO: {[cls.__name__ for cls in Circle.__mro__]}")
    print(f"Rectangle MRO: {[cls.__name__ for cls in Rectangle.__mro__]}")

    # isinstance 和 issubclass
    c = Circle(3)
    print(f"\nisinstance(c, Circle): {isinstance(c, Circle)}")
    print(f"isinstance(c, Shape):  {isinstance(c, Shape)}")
    print(f"issubclass(Circle, Shape): {issubclass(Circle, Shape)}")


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    exercise_user_basics()
    exercise_shapes()
    exercise_team()
    exercise_module_demo()

    print(f"\n{'=' * 60}")
    print("All Day 3 exercises completed!")
    print("=" * 60)
