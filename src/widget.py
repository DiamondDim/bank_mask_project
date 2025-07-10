from datetime import datetime
from typing import Optional, Union


def mask_account_card(account_info: str) -> str:
    """
    Маскирует номер карты или счета в переданной строке.

    Args:
        account_info: Строка с информацией о карте/счете
            (формат: "Visa Platinum 7000792289606361" или "Счет 73654108430135874305")

    Returns:
        Маскированная строка (формат: "Visa Platinum 7000 79** **** 6361" или "Счет **4305")

    Examples:
        >>> mask_account_card("Visa Platinum 7000792289606361")
        'Visa Platinum 7000 79** **** 6361'
        >>> mask_account_card("Счет 73654108430135874305")
        'Счет **4305'
    """
    if not isinstance(account_info, str):
        return "Некорректные данные"

    if "Счет" in account_info:
        parts = account_info.split()
        return f"{parts[0]} **{parts[-1][-4:]}" if len(parts) > 1 else account_info
    else:
        parts = account_info.split()
        number = parts[-1] if len(parts) > 1 else ""
        if len(number) == 16 and number.isdigit():
            return f"{' '.join(parts[:-1])} {number[:4]} {number[4:6]}** **** {number[-4:]}"
        return account_info


def format_date(date_str: Optional[Union[str, int, float]]) -> str:
    """
    Форматирует дату из ISO формата в DD.MM.YYYY.

    Args:
        date_str: Дата в формате ISO (str) или None/число для некорректных данных

    Returns:
        Отформатированная дата или вызывает ValueError при ошибке

    Raises:
        ValueError: Если входные данные некорректны

    Examples:
        >>> format_date("2023-01-01T12:00:00.000000")
        '01.01.2023'
    """
    if not isinstance(date_str, str) or not date_str.strip():
        raise ValueError("Некорректная дата")

    try:
        date_obj = datetime.fromisoformat(date_str)
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError("Некорректная дата")
