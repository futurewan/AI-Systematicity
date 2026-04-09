"""Simple numeric business logic for package structure practice."""


def total_price(unit_price: float, quantity: int) -> float:
    """Return subtotal as unit_price * quantity."""
    return unit_price * quantity


def apply_discount(amount: float, discount_rate: float) -> float:
    """Apply discount using range [0.0, 1.0].

    Example: amount=100, discount_rate=0.2 => 80
    """
    if not 0 <= discount_rate <= 1:
        raise ValueError("discount_rate must be in [0, 1]")
    return amount * (1 - discount_rate)
