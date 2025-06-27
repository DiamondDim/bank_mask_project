from datetime import datetime
from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(data: str) -> str:
    """Маскирует номер карты/счета в строке"""
    if "Счет" in data:
        return f"Счет {get_mask_account(data.split()[-1])}"
    return (f"{' '.join(data.split()[:-1])} "
            f"{get_mask_card_number(data.split()[-1])}")


def get_date(iso_date: str) -> str:
    """Преобразует дату из ISO формата в 'ДД.ММ.ГГГГ'."""

    return datetime.fromisoformat(iso_date).strftime("%d.%m.%Y")
