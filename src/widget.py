from datetime import datetime
from typing import Optional, Union, Any


def mask_account_card(account_info: Any) -> str:
    """
    Маскирует номер карты или счета в переданной строке.

    Args:
        account_info: Может быть строкой с информацией о карте/счете или другим типом

    Returns:
        Маскированная строка или "Некорректные данные" для неподходящих типов
    """
    if not isinstance(account_info, str):
        return "Некорректные данные"

    if "Счет" in account_info:
        parts = account_info.split()
        return f"{parts[0]} **{parts[-1][-4:]}" if len(parts) > 1 else account_info
    else:
        parts = account_info.split()
        number = parts[-1] if len(parts) > 1 else account_info

        if len(number) == 16 and number.isdigit():
            masked = f"{number[:4]} {number[4:6]}** **** {number[-4:]}"
            return f"{' '.join(parts[:-1])} {masked}" if parts[:-1] else masked

        return account_info


def format_date(date_str: Optional[Union[str, int, float]]) -> str:
    """
    Форматирует дату из ISO формата в DD.MM.YYYY.
    """
    if not isinstance(date_str, str) or not date_str.strip():
        raise ValueError("Некорректная дата")

    try:
        date_obj = datetime.fromisoformat(date_str)
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError("Некорректная дата")
