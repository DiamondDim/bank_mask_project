import pytest
from typing import List, Dict, Any
from src.generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator
)


@pytest.fixture
def mixed_transactions() -> List[Dict[str, Any]]:
    """ Фикстура с корректными и некорректными транзакциями """
    return [
        {
            "id": 1,
            "operationAmount": {
                "amount": "100.00",
                "currency": {"code": "USD"}
            },
            "description": "Перевод организации"
        },
        {
            "id": 2,
            "operationAmount": {
                "amount": "200.00",
                "currency": {"code": "EUR"}
            },
            "description": "Перевод со счета на счет"
        },
        None,  # Некорректная транзакция
        {"id": 3},  # Неполная транзакция
        {
            "id": 4,
            "operationAmount": {
                "amount": "300.00",
                "currency": {"code": "USD"}
            },
            "description": "Перевод с карты на карту"
        },
        {
            "operationAmount": {
                "currency": {"code": "GBP"}
            }
        }
    ]


# Тесты для filter_by_currency
@pytest.mark.parametrize("currency,expected_ids", [
    ("USD", [1, 4]),
    ("EUR", [2]),
    ("GBP", [5]),
    ("RUB", []),
], ids=["USD", "EUR", "GBP", "RUB"])
def test_filter_by_currency(
    mixed_transactions: List[Dict[str, Any]],
    currency: str,
    expected_ids: List[int]
) -> None:
    """Тестирует фильтрацию с некорректными данными"""
    result = list(filter_by_currency(mixed_transactions, currency))
    assert [tx.get("id") for tx in result] == expected_ids


def test_filter_by_currency_empty() -> None:
    """Тестирует пустые входные данные"""
    assert list(filter_by_currency([], "USD")) == []
    assert list(filter_by_currency([None, {}], "USD")) == []


# Тесты для transaction_descriptions
def test_transaction_descriptions(mixed_transactions: List[Dict[str, Any]]) -> None:
    """Тестирует получение описаний с некорректными данными"""
    result = list(transaction_descriptions(mixed_transactions))
    assert result == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Нет описания",
        "Нет описания",
        "Перевод с карты на карту",
        "Нет описания"
    ]


# Тесты для card_number_generator
@pytest.mark.parametrize("start,end,step,expected", [
    (1, 5, 1, [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005"
    ]),
    (1, 10, 2, [
        "0000 0000 0000 0001",
        "0000 0000 0000 0003",
        "0000 0000 0000 0005",
        "0000 0000 0000 0007",
        "0000 0000 0000 0009"
    ]),
    (9995, 9999, 1, [
        "0000 0000 0000 9995",
        "0000 0000 0000 9996",
        "0000 0000 0000 9997",
        "0000 0000 0000 9998",
        "0000 0000 0000 9999"
    ]),
], ids=["sequential", "step_2", "high_numbers"])
def test_card_number_generator(
    start: int,
    end: int,
    step: int,
    expected: List[str]
) -> None:
    """Тестирует генерацию номеров с разными параметрами"""
    assert list(card_number_generator(start, end, step=step)) == expected


@pytest.mark.parametrize("start,end,step", [
    (0, 5, 1),    # start < 1
    (5, 1, 1),    # end < start
    (1, 5, 0),    # step < 1
    (1, 5, -1),   # negative step
], ids=["low_start", "reverse_range", "zero_step", "negative_step"])
def test_card_number_generator_invalid(
    start: int,
    end: int,
    step: int
) -> None:
    """Тестирует обработку невалидных параметров"""
    with pytest.raises(ValueError):
        list(card_number_generator(start, end, step=step))


def test_card_number_custom_format() -> None:
    """Тестирует кастомный формат вывода"""
    result = list(card_number_generator(1, 1, card_format="XX-XX-XXXX"))
    assert result == ["00-00-0001"]
