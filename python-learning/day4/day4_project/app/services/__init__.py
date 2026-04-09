"""Service layer package."""

from .calculator import apply_discount, total_price
from .text_service import normalize_name

__all__ = ["apply_discount", "total_price", "normalize_name"]
