"""Day 3 models: OOP classes for User, Shape, Team.

This module is designed to be imported by day3_exercises.py.
It also works standalone for quick testing.

Run standalone:
    python3 python-learning/day3/day3_models.py

JS 开发者逐行对照版说明：
- 目标：尽量让每个关键 Python 语句旁边都能看到 JS 心智映射。
- 原则：只加注释，不改逻辑。
"""

import math  # Python 标准数学库；JS 对照：内置 `Math` 对象（如 `Math.PI`）。


# ---------------------------------------------------------------------------
# 1. User class - basics of __init__, __str__, __repr__, @property, methods
# ---------------------------------------------------------------------------
class User:  # JS 对照：`class User { ... }`
    """Represents a system user with role-based promotion.

    Attributes:
        name:  user display name
        email: user email address
        role:  one of 'viewer', 'editor', 'admin'
    """

    ROLE_LADDER = ["viewer", "editor", "admin"]  # JS 对照：`static ROLE_LADDER = [...]`

    def __init__(self, name: str, email: str, role: str = "viewer") -> None:
        # JS 对照：constructor(name, email, role = "viewer") { ... }
        self.name = name  # JS 对照：`this.name = name`
        self.email = email  # JS 对照：`this.email = email`
        if role not in self.ROLE_LADDER:  # JS 对照：`if (!User.ROLE_LADDER.includes(role))`
            raise ValueError(f"Invalid role: {role}. Must be one of {self.ROLE_LADDER}")  # JS 对照：throw new Error(...)
        self.role = role  # JS 对照：`this.role = role`

    def __str__(self) -> str:
        # JS 类比：对象的 `toString()`，但 Python 的 `print(obj)` 会优先走 `__str__`
        return f"User(name={self.name}, role={self.role})"  # JS 对照：`return \`User(name=${this.name}, role=${this.role})\``

    def __repr__(self) -> str:
        # JS 类比：更偏调试输出，接近你手工写的 debug 字符串
        return f"User('{self.name}', '{self.email}', '{self.role}')"  # Python 容器打印对象常用 repr

    @property  # JS 对照：`get emailDomain() { ... }`
    def email_domain(self) -> str:
        # Python 调用方式：u.email_domain（不是 u.email_domain()）
        return self.email.split("@")[1]  # JS 对照：`this.email.split("@")[1]`

    def promote(self) -> None:
        # JS 对照：const currentIndex = User.ROLE_LADDER.indexOf(this.role)
        current_index = self.ROLE_LADDER.index(self.role)
        # JS 对照：if (currentIndex >= User.ROLE_LADDER.length - 1) { throw new Error(...) }
        if current_index >= len(self.ROLE_LADDER) - 1:
            raise ValueError(f"User '{self.name}' is already an admin, cannot promote further.")
        # JS 对照：this.role = User.ROLE_LADDER[currentIndex + 1]
        self.role = self.ROLE_LADDER[current_index + 1]


# ---------------------------------------------------------------------------
# 2. Shape hierarchy - inheritance and polymorphism
# ---------------------------------------------------------------------------
class Shape:  # JS 对照：`class Shape { ... }`
    """所有形状的基类。"""

    def __init__(self, name: str) -> None:
        self.name = name  # JS 对照：`this.name = name`

    def area(self) -> float:
        # JS 对照：throw new Error("Subclass must implement area()")
        raise NotImplementedError("Subclass must implement area()")

    def describe(self) -> str:
        # `:.2f` 表示保留 2 位小数；JS 对照：`this.area().toFixed(2)`
        return f"{self.name}: area = {self.area():.2f}"


class Circle(Shape):  # JS 对照：`class Circle extends Shape`
    """圆形，继承自 Shape。"""

    def __init__(self, radius: float) -> None:
        super().__init__("Circle")  # JS 对照：`super("Circle")`
        self.radius = radius  # JS 对照：`this.radius = radius`

    def area(self) -> float:
        return math.pi * self.radius ** 2  # JS 对照：`Math.PI * this.radius ** 2`

    def __str__(self) -> str:
        return f"Circle(radius={self.radius})"  # JS 对照：`return \`Circle(radius=${this.radius})\``


class Rectangle(Shape):  # JS 对照：`class Rectangle extends Shape`
    """矩形，继承自 Shape。"""

    def __init__(self, width: float, height: float) -> None:
        super().__init__("Rectangle")  # JS 对照：`super("Rectangle")`
        self.width = width  # JS 对照：`this.width = width`
        self.height = height  # JS 对照：`this.height = height`

    def area(self) -> float:
        return self.width * self.height  # JS 对照：`return this.width * this.height`

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"  # JS 对照模板字符串


# ---------------------------------------------------------------------------
# 3. Team class - composition pattern (has-a relationship)
# ---------------------------------------------------------------------------
class Team:  # JS 对照：`class Team { ... }`
    """团队类，演示组合模式（Team 包含多个 User）。"""

    def __init__(self, name: str) -> None:
        self.name = name  # JS 对照：`this.name = name`
        self._members: list[User] = []  # JS 对照：`this._members = []`（约定私有，不是语法私有）

    def add_member(self, user: User) -> None:
        # 集合推导式；JS 对照：`new Set(this._members.map(m => m.email))`
        existing_emails = {m.email for m in self._members}
        if user.email in existing_emails:  # JS 对照：`if (existingEmails.has(user.email))`
            raise ValueError(f"User with email '{user.email}' already in team '{self.name}'.")
        self._members.append(user)  # JS 对照：`this._members.push(user)`

    def find_by_role(self, role: str) -> list[User]:
        # 列表推导式；JS 对照：`return this._members.filter(m => m.role === role)`
        return [m for m in self._members if m.role == role]

    def __len__(self) -> int:
        # 实现后可以 `len(team)`；JS 里通常会写 `team.members.length` 或 getter
        return len(self._members)

    def __str__(self) -> str:
        # 生成器表达式 + join；JS 对照：`this._members.map(m => m.name).join(", ")`
        member_names = ", ".join(m.name for m in self._members)
        return f"Team({self.name}, members=[{member_names}])"


# ---------------------------------------------------------------------------
# Standalone test (when running this file directly)
# ---------------------------------------------------------------------------
if __name__ == "__main__":  # JS 对照：`if (require.main === module)`
    print("=== day3_models.py standalone test ===")  # JS 对照：`console.log(...)`

    u = User("Alice", "alice@example.com")  # JS 对照：`const u = new User(...)`
    print(u)  # JS 对照：`console.log(u.toString())`（类比）
    print(f"email_domain: {u.email_domain}")  # JS 对照：`console.log(\`email_domain: ${u.emailDomain}\`)`
    u.promote()  # JS 对照：`u.promote()`
    print(f"After promote: {u}")  # JS 对照模板字符串

    c = Circle(5)  # JS 对照：`const c = new Circle(5)`
    print(c.describe())  # JS 对照：`console.log(c.describe())`

    r = Rectangle(3, 4)  # JS 对照：`const r = new Rectangle(3, 4)`
    print(r.describe())  # JS 对照：`console.log(r.describe())`
