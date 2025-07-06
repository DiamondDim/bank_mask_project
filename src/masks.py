def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты в формате XXXX XX** **** XXXX

    Args:
        card_number: Номер карты (16 цифр)

    Returns:
        Замаскированная строка (или пустая строка для пустого ввода)
    """
    if not card_number:
        return ""
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Номер карты должен содержать 16 цифр")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета в формате **XXXX

    Args:
        account_number: Номер счета (минимум 4 цифры)

    Returns:
        Замаскированная строка (или пустая строка для пустого ввода)
    """
    if not account_number:
        return ""
    if len(account_number) < 4 or not account_number.isdigit():
        raise ValueError("Номер счета должен содержать минимум 4 цифры")
    return f"**{account_number[-4:]}"
