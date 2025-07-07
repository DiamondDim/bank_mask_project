from typing import Union


def mask_card_number(card_number: Union[str, int]) -> str:
    """
    Маскирует номер карты, сохраняя первые 6 и последние 4 цифры.

    Args:
        card_number: Номер карты (16 цифр) в виде строки или числа

    Returns:
        Маскированный номер в формате "XXXX XX** **** XXXX"

    Raises:
        ValueError: Если номер не содержит 16 цифр

    Examples:
        >>> mask_card_number("7000792289606361")
        '7000 79** **** 6361'
    """
    num_str = str(card_number).strip()
    if len(num_str) != 16 or not num_str.isdigit():
        raise ValueError("Номер карты должен содержать 16 цифр")
    return f"{num_str[:4]} {num_str[4:6]}** **** {num_str[-4:]}"


def mask_account_number(account_number: Union[str, int]) -> str:
    """
    Маскирует номер счета, показывая только последние 4 цифры.

    Args:
        account_number: Номер счета (минимум 4 цифры)

    Returns:
        Маскированный номер в формате "**XXXX"

    Raises:
        ValueError: Если номер содержит меньше 4 цифр

    Examples:
        >>> mask_account_number("73654108430135874305")
        '**4305'
    """
    num_str = str(account_number).strip()
    if len(num_str) < 4 or not num_str.isdigit():
        raise ValueError("Номер счета должен содержать минимум 4 цифры")
    return f"**{num_str[-4:]}"
