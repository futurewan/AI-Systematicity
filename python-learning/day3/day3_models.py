"""Day 3 models: OOP classes for User, Shape, Team.

This module is designed to be imported by day3_exercises.py.
It also works standalone for quick testing.

Run standalone:
    python3 python-learning/day3/day3_models.py
"""

import math


# ---------------------------------------------------------------------------
# 1. User class - basics of __init__, __str__, __repr__, @property, methods
# ---------------------------------------------------------------------------
class User:
    """Represents a system user with role-based promotion.

    Attributes:
        name:  user display name
        email: user email address
        role:  one of 'viewer', 'editor', 'admin'
    """

    # 定义角色升级路径（类变量，所有实例共享）
    ROLE_LADDER = ["viewer", "editor", "admin"]

    def __init__(self, name: str, email: str, role: str = "viewer") -> None:
        """初始化 User 实例。

        Args:
            name:  用户名
            email: 邮箱地址
            role:  角色，默认 'viewer'
        """
        self.name = name
        self.email = email
        # 校验 role 是否合法
        if role not in self.ROLE_LADDER:
            raise ValueError(f"Invalid role: {role}. Must be one of {self.ROLE_LADDER}")
        self.role = role

    def __str__(self) -> str:
        """用户友好的字符串表示，适合 print() 输出。"""
        return f"User(name={self.name}, role={self.role})"

    def __repr__(self) -> str:
        """开发者友好的字符串表示，适合调试。
        repr 与 str 的区别：
        - __str__：面向用户，可读性优先
        - __repr__：面向开发者，应能重建对象
        """
        return f"User('{self.name}', '{self.email}', '{self.role}')"

    @property
    def email_domain(self) -> str:
        """提取邮箱地址的域名部分。

        @property 装饰器：让方法像属性一样被访问
        用法：user.email_domain（不需要加括号）
        """
        return self.email.split("@")[1]

    def promote(self) -> None:
        """将用户角色提升一级。

        viewer -> editor -> admin
        如果已是 admin，抛出 ValueError。
        """
        current_index = self.ROLE_LADDER.index(self.role)
        if current_index >= len(self.ROLE_LADDER) - 1:
            raise ValueError(f"User '{self.name}' is already an admin, cannot promote further.")
        self.role = self.ROLE_LADDER[current_index + 1]


# ---------------------------------------------------------------------------
# 2. Shape hierarchy - inheritance and polymorphism
# ---------------------------------------------------------------------------
class Shape:
    """所有形状的基类。

    子类必须实现 area() 方法来提供具体的面积计算逻辑。
    """

    def __init__(self, name: str) -> None:
        self.name = name

    def area(self) -> float:
        """计算面积（子类必须重写此方法）。"""
        raise NotImplementedError("Subclass must implement area()")

    def describe(self) -> str:
        """返回形状的描述信息，包含名称和面积。"""
        return f"{self.name}: area = {self.area():.2f}"


class Circle(Shape):
    """圆形，继承自 Shape。"""

    def __init__(self, radius: float) -> None:
        # super() 调用父类的 __init__，设置 name
        super().__init__("Circle")
        self.radius = radius

    def area(self) -> float:
        """圆面积 = π * r²"""
        return math.pi * self.radius ** 2

    def __str__(self) -> str:
        return f"Circle(radius={self.radius})"


class Rectangle(Shape):
    """矩形，继承自 Shape。"""

    def __init__(self, width: float, height: float) -> None:
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self) -> float:
        """矩形面积 = 宽 * 高"""
        return self.width * self.height

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"


# ---------------------------------------------------------------------------
# 3. Team class - composition pattern (has-a relationship)
# ---------------------------------------------------------------------------
class Team:
    """团队类，演示组合模式（Team 包含多个 User）。

    组合 vs 继承：
    - 继承（is-a）：Circle 是一个 Shape
    - 组合（has-a）：Team 有多个 User
    """

    def __init__(self, name: str) -> None:
        self.name = name
        self._members: list[User] = []  # 私有属性，用 _ 前缀约定

    def add_member(self, user: User) -> None:
        """添加成员（邮箱不能重复）。

        Args:
            user: 要添加的用户

        Raises:
            ValueError: 如果该邮箱已存在于团队中
        """
        # 检查邮箱是否已存在
        existing_emails = {m.email for m in self._members}
        if user.email in existing_emails:
            raise ValueError(f"User with email '{user.email}' already in team '{self.name}'.")
        self._members.append(user)

    def find_by_role(self, role: str) -> list[User]:
        """根据角色筛选成员。

        Args:
            role: 要筛选的角色名

        Returns:
            符合角色的用户列表
        """
        return [m for m in self._members if m.role == role]

    def __len__(self) -> int:
        """返回团队人数，使得 len(team) 可用。"""
        return len(self._members)

    def __str__(self) -> str:
        member_names = ", ".join(m.name for m in self._members)
        return f"Team({self.name}, members=[{member_names}])"


# ---------------------------------------------------------------------------
# Standalone test (when running this file directly)
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=== day3_models.py standalone test ===")

    u = User("Alice", "alice@example.com")
    print(u)
    print(f"email_domain: {u.email_domain}")
    u.promote()
    print(f"After promote: {u}")

    c = Circle(5)
    print(c.describe())

    r = Rectangle(3, 4)
    print(r.describe())
