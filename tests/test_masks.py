import pytest
from typing import List
from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def sample_cards() -> List[str]:
    return [
        "7000792289606361",  # Visa
        "1234567890123456",  # Mastercard
        "",  # Пустая строка
        "4111111111111111"  # Visa
    ]


@pytest.fixture
def sample_accounts() -> List[str]:
    return [
        "73654108430135874305",
        "",  # Пустая строка
        "40817810500001234567"
    ]


@pytest.mark.parametrize("card_number, expected", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("1234567890123456", "1234 56** **** 3456"),
    ("", ""),  # Явная проверка пустой строки
    ("4111111111111111", "4111 11** **** 1111"),
], ids=["visa", "mastercard", "empty", "visa2"])
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    """Тестирует маскировку номеров карт, включая пустую строку"""
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("account_number, expected", [
    ("73654108430135874305", "**4305"),
    ("", ""),  # Явная проверка пустой строки
    ("40817810500001234567", "**4567"),
], ids=["account1", "empty", "account2"])
def test_get_mask_account(account_number: str, expected: str) -> None:
    """Тестирует маскировку номеров счетов, включая пустую строку"""
    assert get_mask_account(account_number) == expected


def test_mask_card_edge_cases() -> None:
    """Тестирует крайние случаи для карт"""
    # Пустая строка (дополнительная проверка)
    assert get_mask_card_number("") == ""

    # Невалидные данные
    with pytest.raises(ValueError):
        get_mask_card_number("123")  # Слишком короткий


def test_mask_account_edge_cases() -> None:
    """Тестирует крайние случаи для счетов"""
    # Пустая строка (дополнительная проверка)
    assert get_mask_account("") == ""

    # Невалидные данные
    with pytest.raises(ValueError):
        get_mask_account("123")  # Слишком короткий
