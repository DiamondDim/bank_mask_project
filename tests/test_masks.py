from typing import NoReturn

import pytest

from src.masks import mask_account_number, mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1234567890123456", "1234 56** **** 3456"),
        ("", ""),  # Пустая строка
        ("4111111111111111", "4111 11** **** 1111"),
    ],
    ids=["visa", "mastercard", "empty", "visa2"],
)
def test_mask_card_number(card_number: str, expected: str) -> None:
    """
    Тестирует основную функциональность маскировки номеров карт.

    Проверяет:
    - Корректную маскировку валидных номеров
    - Обработку пустой строки
    - Соответствие ожидаемому формату

    Args:
        card_number: Входной номер карты для тестирования
        expected: Ожидаемый результат после маскировки
    """
    assert mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("73654108430135874305", "**4305"),
        ("", ""),  # Пустая строка
        ("40817810500001234567", "**4567"),
    ],
    ids=["account1", "empty", "account2"],
)
def test_mask_account_number(account_number: str, expected: str) -> None:
    """
    Тестирует основную функциональность маскировки номеров счетов.

    Проверяет:
    - Корректную маскировку валидных номеров
    - Обработку пустой строки
    - Соответствие формату **XXXX

    Args:
        account_number: Входной номер счета для тестирования
        expected: Ожидаемый результат после маскировки
    """
    assert mask_account_number(account_number) == expected


def test_mask_card_edge_cases() -> None:
    """
    Тестирует обработку крайних случаев для номеров карт.

    Проверяет:
    - Вызов исключения для слишком коротких номеров
    """
    with pytest.raises(ValueError):
        mask_card_number("123")
    return None


def test_mask_empty_input() -> None:
    assert mask_card_number("") == ""
    return None


def test_mask_account_edge_cases() -> NoReturn:
    """
    Тестирует обработку крайних случаев для номеров счетов.

    Проверяет:
    - Вызов исключения для слишком коротких номеров
    - Вызов исключения для нечисловых значений
    """
    with pytest.raises(ValueError, match="Номер счета должен содержать минимум 4 цифры"):
        mask_account_number("123")  # Слишком короткий номер

    with pytest.raises(ValueError, match="Номер счета должен содержать минимум 4 цифры"):
        mask_account_number("abcd")  # Нечисловое значение
