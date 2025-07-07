import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("card_number, expected", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("1234567890123456", "1234 56** **** 3456"),
    ("", ""),
    ("4111111111111111", "4111 11** **** 1111"),
], ids=["visa", "mastercard", "empty", "visa2"])
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    """Тестирует маскировку номеров карт с различными входами"""
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("account_number, expected", [
    ("73654108430135874305", "**4305"),
    ("", ""),
    ("40817810500001234567", "**4567"),
], ids=["account1", "empty", "account2"])
def test_get_mask_account(account_number: str, expected: str) -> None:
    """Тестирует маскировку номеров счетов с различными входами"""
    assert get_mask_account(account_number) == expected


def test_mask_card_edge_cases() -> None:
    """Тестирует крайние случаи для маскировки карт"""
    # Пустая строка
    assert get_mask_card_number("") == ""
    # Невалидные номера
    with pytest.raises(ValueError):
        get_mask_card_number("123")
    with pytest.raises(ValueError):
        get_mask_card_number("abcdefghijklmnop")


def test_mask_account_edge_cases() -> None:
    """Тестирует крайние случаи для маскировки счетов"""
    # Пустая строка
    assert get_mask_account("") == ""
    # Невалидные номера
    with pytest.raises(ValueError):
        get_mask_account("123")
    with pytest.raises(ValueError):
        get_mask_account("abcd")


def test_mask_card_format() -> None:
    """Тестирует правильность формата маскированной карты"""
    masked = get_mask_card_number("1234567890123456")
    parts = masked.split()
    assert len(parts) == 4
    assert len(parts[0]) == 4  # Первые 4 цифры
    assert len(parts[1]) == 4 and "**" in parts[1]  # Две цифры и две звездочки
    assert parts[2] == "****"  # Четыре звездочки
    assert len(parts[3]) == 4  # Последние 4 цифры


def test_mask_account_format() -> None:
    """Тестирует правильность формата маскированного счета"""
    masked = get_mask_account("1234567890")
    assert masked.startswith("**")
    assert len(masked) == 6  # 2 звездочки + 4 цифры
    assert masked[2:].isdigit()


def test_mask_account_invalid():
    with pytest.raises(ValueError):
        get_mask_account("123")  # Менее 4 цифр


def test_mask_empty_input():
    """Тест обработки пустого ввода"""
    assert get_mask_card_number("") == ""
    assert get_mask_account("") == ""
