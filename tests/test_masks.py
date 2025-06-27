import pytest
from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number() -> None:
    """Тестирование функции маскировки номера банковской карты. """
    # Проверка корректного номера
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"

    # Проверка ошибок
    with pytest.raises(ValueError, match="16 цифр"):
        get_mask_card_number("123")  # Слишком короткий
    with pytest.raises(ValueError):
        get_mask_card_number("abcdefghijklmnop")  # Не цифры


def test_get_mask_account() -> None:
    """Тестирование функции маскировки счёта. """
    # Проверка корректного номера
    assert get_mask_account("73654108430135874305") == "**4305"

    # Проверка ошибок
    with pytest.raises(ValueError, match="4 цифры"):
        get_mask_account("123")  # Слишком короткий
    with pytest.raises(ValueError):
        get_mask_account("abcde")  # Не цифры
