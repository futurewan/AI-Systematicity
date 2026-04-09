"""Main app entry for package import demonstrations."""

from .config import APP_NAME, DEFAULT_CURRENCY
from .services import apply_discount, normalize_name, total_price
from .utils import is_positive_int


def run_app_demo() -> dict[str, str | float | bool]:
    """Run a small deterministic scenario for tests/exercises."""
    raw_name = "  maple lee  "
    name = normalize_name(raw_name)

    quantity = 3
    if not is_positive_int(quantity):
        raise ValueError("quantity must be a positive int")

    subtotal = total_price(99.0, quantity)
    final_price = apply_discount(subtotal, 0.1)

    return {
        "app": APP_NAME,
        "user": name,
        "currency": DEFAULT_CURRENCY,
        "subtotal": round(subtotal, 2),
        "final": round(final_price, 2),
    }


if __name__ == "__main__":
    print(run_app_demo())
