import pytest
from typing import Dict, List, Any
from src.generators import filter_by_currency, transaction_descriptions


@pytest.fixture
def transactions_mixed() -> List[Dict[str, Any]]:
    """Фикстура с валидными транзакциями (без None)."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01", "currency": "USD"},
        {"id": 2, "state": "CANCELED", "date": "2023-02-01", "currency": "EUR"},
        {"id": 3, "state": "EXECUTED", "date": "2023-03-01", "currency": "USD"},
    ]


@pytest.fixture
def transactions_empty() -> List[Dict[str, Any]]:
    """Фикстура с пустым списком (вместо None)."""
    return []


def test_filter_by_currency(transactions_mixed: List[Dict[str, Any]]) -> None:
    """Тест фильтрации по валюте."""
    usd_transactions = list(filter_by_currency(transactions_mixed, "USD"))
    assert len(usd_transactions) == 2
    assert all(t["currency"] == "USD" for t in usd_transactions)


def test_transaction_descriptions(transactions_mixed: List[Dict[str, Any]]) -> None:
    """Тест генератора описаний транзакций."""
    descriptions = list(transaction_descriptions(transactions_mixed))
    assert len(descriptions) == 3
    assert isinstance(descriptions[0], str)
