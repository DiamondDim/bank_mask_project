from typing import Any, Dict, List

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def sample_transactions() -> List[Dict[str, Any]]:
    """Фикстура с тестовыми данными транзакций."""
    return [
        {
            "id": 1,
            "operationAmount": {"amount": "100.00", "currency": {"code": "USD", "name": "US Dollar"}},
            "description": "Payment 1",
        },
        {
            "id": 2,
            "operationAmount": {"amount": "200.00", "currency": {"code": "EUR", "name": "Euro"}},
            "description": "Payment 2",
        },
        {
            "id": 3,
            "operationAmount": {"amount": "300.00", "currency": {"code": "USD", "name": "US Dollar"}},
            "description": "Payment 3",
        },
        {
            "id": 4,
            "operationAmount": {"amount": "400.00", "currency": {"code": "GBP", "name": "Pound Sterling"}},
            "description": "Payment 4",
        },
    ]


def test_filter_by_currency_usd(sample_transactions: List[Dict[str, Any]]) -> None:
    """Тест фильтрации транзакций по USD."""
    usd_transactions = list(filter_by_currency(sample_transactions, "USD"))
    assert len(usd_transactions) == 2
    assert all(t["operationAmount"]["currency"]["code"] == "USD" for t in usd_transactions)


def test_filter_by_currency_eur(sample_transactions: List[Dict[str, Any]]) -> None:
    """Тест фильтрации транзакций по EUR."""
    eur_transactions = list(filter_by_currency(sample_transactions, "EUR"))
    assert len(eur_transactions) == 1
    assert eur_transactions[0]["id"] == 2


def test_filter_by_currency_empty_list() -> None:
    """Тест фильтрации пустого списка транзакций."""
    assert list(filter_by_currency([], "USD")) == []


def test_filter_by_currency_no_matches(sample_transactions: List[Dict[str, Any]]) -> None:
    """Тест фильтрации при отсутствии совпадений."""
    assert list(filter_by_currency(sample_transactions, "JPY")) == []


def test_filter_by_currency_invalid_transaction() -> None:
    """Тест обработки некорректных транзакций."""
    transactions: List[Dict[str, Any]] = [{"id": 1}, {"operationAmount": {}}]
    assert list(filter_by_currency(transactions, "USD")) == []


def test_transaction_descriptions(sample_transactions: List[Dict[str, Any]]) -> None:
    """Тест генератора описаний транзакций."""
    descriptions = list(transaction_descriptions(sample_transactions))
    assert descriptions == ["Payment 1", "Payment 2", "Payment 3", "Payment 4"]


def test_transaction_descriptions_empty() -> None:
    """Тест генератора описаний с пустым списком."""
    assert list(transaction_descriptions([])) == []


def test_card_number_generator_basic() -> None:
    """Тест генератора номеров карт (базовый случай)."""
    numbers = list(card_number_generator(1, 5))
    assert numbers == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]


def test_card_number_generator_large_numbers() -> None:
    """Тест генератора номеров карт (большие числа)."""
    numbers = list(card_number_generator(9999999999999995, 9999999999999999))
    assert numbers == [
        "9999 9999 9999 9995",
        "9999 9999 9999 9996",
        "9999 9999 9999 9997",
        "9999 9999 9999 9998",
        "9999 9999 9999 9999",
    ]


def test_card_number_generator_single() -> None:
    """Тест генератора номеров карт (один номер)."""
    assert list(card_number_generator(42, 42)) == ["0000 0000 0000 0042"]


def test_filter_by_currency_invalid_structure() -> None:
    transactions = [{"operationAmount": "not-a-dict"}]
    assert list(filter_by_currency(transactions, "USD")) == []


def test_filter_by_currency_edge_cases() -> None:
    """Тест на нестандартные структуры данных"""
    # 1. Не словарь transaction
    assert list(filter_by_currency([None, "not-a-dict"], "USD")) == []

    # 2. Некорректный operationAmount
    assert list(filter_by_currency([{"operationAmount": None}], "USD")) == []

    # 3. Некорректный currency
    assert list(filter_by_currency([{"operationAmount": {"currency": "not-a-dict"}}], "USD")) == []


def test_filter_by_currency_invalid_data() -> None:
    assert list(filter_by_currency([None, "string"], "USD")) == []
    assert list(filter_by_currency([{"operationAmount": None}], "USD")) == []
    assert list(filter_by_currency([{"operationAmount": {}}], "USD")) == []
