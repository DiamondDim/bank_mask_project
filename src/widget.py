from datetime import datetime
from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(data: str) -> str:
    """Маскирует номер карты/счета в строке"""
    if "Счет" in data:
        return f"Счет {get_mask_account(data.split()[-1])}"
    return (f"{' '.join(data.split()[:-1])} "
            f"{get_mask_card_number(data.split()[-1])}")


def format_date(date_str: str) -> str:
    """
    Форматирует дату из ISO формата в DD.MM.YYYY

    Args:
        date_str: Дата в формате ISO (YYYY-MM-DDTHH:MM:SS.ffffff)

    Returns:
        Строка с датой в формате DD.MM.YYYY
    """
    date_obj = datetime.fromisoformat(date_str)
    return date_obj.strftime("%d.%m.%Y")


def mask_account_card(account_info: str) -> str:
    """
    Маскирует номер карты или счета в строке.

    Args:
        account_info: Строка с информацией о карте/счете

    Returns:
        Маскированная строка
    """
    if "Счет" in account_info:
        # Маскировка счета
        parts = account_info.split()
        return f"{parts[0]} **{parts[1][-4:]}"
    else:
        # Маскировка карты
        parts = account_info.split()
        number = parts[-1]
        return f"{' '.join(parts[:-1])} {number[:4]} {number[4:6]}** **** {number[-4:]}"


def format_date(date_str: str) -> str:
    """
    Форматирует дату из ISO формата в DD.MM.YYYY

    Args:
        date_str: Дата в формате ISO

    Returns:
        Строка с датой в формате DD.MM.YYYY
    """
    try:
        date_obj = datetime.fromisoformat(date_str)
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        return "Некорректная дата"