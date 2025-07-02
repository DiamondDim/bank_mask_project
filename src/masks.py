def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты в формате XXXX XX** **** XXXX.
    Поддерживает пустые строки.

    Args:
        card_number: Номер карты (16+ цифр). Пустая строка допускается.

    Returns:
        - Пустую строку для пустого ввода
        - Замаскированный номер карты для валидного ввода

    Raises:
        ValueError: Если номер содержит не-цифры или <16 цифр
    """
    if not card_number:
        return ""

    if not card_number.isdigit():
        raise ValueError("Номер карты должен содержать только цифры")

    if len(card_number) < 16:
        raise ValueError("Номер карты должен содержать минимум 16 цифр")

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета в формате **XXXX.
    Поддерживает пустые строки.

    Args:
        account_number: Номер счета (4+ цифр). Пустая строка допускается.

    Returns:
        - Пустую строку для пустого ввода
        - **XXXX для валидных номеров

    Raises:
        ValueError: Если ввод содержит не-цифры или 1-3 цифры
    """
    if not account_number:
        return ""

    if not account_number.isdigit():
        raise ValueError("Номер счета должен содержать только цифры")

    if len(account_number) < 4:
        raise ValueError("Номер счета должен содержать минимум 4 цифры")

    return "**" + account_number[-4:]