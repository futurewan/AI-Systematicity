class User:
    ROLE_LADDER = ["viewer", "editor", "admin"]

    def __init__(self, name: str, email: str, role: str = "viewer") -> None:
        self.name = name
        self.email = email

        if role not in self.ROLE_LADDER:
            raise ValueError(f"Invalid role: {role}. Must be one of {self.ROLE_LADDER}")
        self.role = role

    def __str__(self) -> str:
        return f"User(name={self.name}, role={self.role})"

    def __repr__(self) -> str:
        return f"User('{self.name}', '{self.email}', '{self.role}')"

    @property
    def email_domain(self) -> str:
        return self.email.split("@")[1]

    def promote(self) -> None:
        current_index = self.ROLE_LADDER.index(self.role)
        if current_index >= len(self.ROLE_LADDER) - 1:
            raise ValueError(
                f"User '{self.name}' is already an admin, cannot promote further."
            )
        self.role = self.ROLE_LADDER[current_index + 1]
        print(f"Promoted {self.name} to {self.role}")
