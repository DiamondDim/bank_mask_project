import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("card_number, expected", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("1234567890123456", "1234 56** **** 3456"),
    ("", ""),  # Пустая строка
    ("4111111111111111", "4111 11** **** 1111"),
], ids=["visa", "mastercard", "empty", "visa2"])
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    """Тестирует маскировку номеров карт, включая пустую строку"""
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("account_number, expected", [
    ("73654108430135874305", "**4305"),
    ("", ""),  # Пустая строка
    ("40817810500001234567", "**4567"),
], ids=["account1", "empty", "account2"])
def test_get_mask_account(account_number: str, expected: str) -> None:
    """Тестирует маскировку номеров счетов, включая пустую строку"""
    assert get_mask_account(account_number) == expected


def test_mask_card_edge_cases() -> None:
    """Тестирует крайние случаи для карт"""
    # Пустая строка
    assert get_mask_card_number("") == ""
    # Невалидные номера
    with pytest.raises(ValueError):
        get_mask_card_number("123")
    with pytest.raises(ValueError):
        get_mask_card_number("abcdefghijklmnop")


def test_mask_account_edge_cases() -> None:
    """Тестирует крайние случаи для счетов"""
    # Пустая строка
    assert get_mask_account("") == ""
    # Невалидные номера
    with pytest.raises(ValueError):
        get_mask_account("123")
    with pytest.raises(ValueError):
        get_mask_account("abcd")


def test_mask_card_valid_length() -> None:
    """Тест правильной длины маскированного номера карты"""
    masked = get_mask_card_number("1234567890123456")
    assert len(masked.replace(" ", "")) == 16 + 7  # 16 цифр + 7 символов маски


def test_mask_account_valid_length() -> None:
    """Тест правильной длины маскированного счета"""
    masked = get_mask_account("1234567890")
    assert len(masked) == 6  # 2 звездочки + 4 цифры
