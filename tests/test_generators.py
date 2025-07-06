import pytest
from typing import List, Dict, Any
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def sample_transactions() -> List[Dict[str, Any]]:
    """Фикстура с тестовыми данными транзакций."""
    return [
        {
            "id": 1,
            "operationAmount": {
                "amount": "100.00",
                "currency": {"code": "USD"}
            },
            "description": "Перевод организации",
            "state": "EXECUTED"
        },
        {
            "id": 2,
            "operationAmount": {
                "amount": "200.00",
                "currency": {"code": "EUR"}
            },
            "description": "Перевод со счета на счет",
            "state": "EXECUTED"
        },
        {
            "id": 3,
            "operationAmount": {
                "amount": "300.00",
                "currency": {"code": "USD"}
            },
            "description": "Перевод с карты на карту",
            "state": "CANCELED"
        }
    ]


def test_filter_by_currency(sample_transactions: List[Dict[str, Any]]) -> None:
    """Тестирует фильтрацию транзакций по валюте."""
    # Тест USD-транзакций
    usd_transactions = list(filter_by_currency(sample_transactions, "USD"))
    assert len(usd_transactions) == 2
    assert all(tx["operationAmount"]["currency"]["code"] == "USD" for tx in usd_transactions)

    # Тест пустого результата
    assert len(list(filter_by_currency(sample_transactions, "GBR"))) == 0


def test_transaction_descriptions(sample_transactions: List[Dict[str, Any]]) -> None:
    """Тестирует получение описаний транзакций."""
    descriptions = list(transaction_descriptions(sample_transactions))
    assert descriptions == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод с карты на карту"
    ]

    # Тест пустого списка
    assert len(list(transaction_descriptions([]))) == 0


@pytest.mark.parametrize("start,end,expected", [
    (1, 1, ["0000 0000 0000 0001"]),
    (1, 3, [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003"
    ]),
    (9999999999999996, 9999999999999999, [
        "9999 9999 9999 9996",
        "9999 9999 9999 9997",
        "9999 9999 9999 9998",
        "9999 9999 9999 9999"
    ])
])
def test_card_number_generator(start: int, end: int, expected: List[str]) -> None:
    """Тестирует генератор номеров карт."""
    assert list(card_number_generator(start, end)) == expected


def test_filter_by_currency_edge_cases() -> None:
    """Тестирует крайние случаи фильтрации."""
    # Пустой список транзакций
    assert len(list(filter_by_currency([], "USD"))) == 0

    # Некорректная структура данных
    assert len(list(filter_by_currency([{"operationAmount": {}}], "USD"))) == 0


def test_card_number_generator_edges() -> None:
    """Тестирует граничные значения генератора карт."""
    cards = list(card_number_generator(1, 2))
    assert cards == ["0000 0000 0000 0001", "0000 0000 0000 0002"]

    # Большой диапазон
    assert len(list(card_number_generator(1, 100))) == 100
