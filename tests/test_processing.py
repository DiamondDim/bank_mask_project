import pytest
from typing import Dict, List, Any
from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_transactions() -> List[Dict[str, Any]]:
    """Фикстура с тестовыми данными (без None и пустых словарей)."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01T00:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2023-02-01T00:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2023-03-01T00:00:00"},
    ]


def test_filter_by_state_with_empty() -> None:
    """Тест фильтрации с некорректными данными (пустые словари и None отфильтровываются)."""
    transactions: List[Dict[str, Any]] = [
        {"state": "EXECUTED"},
        {},  # Будет отфильтрован (нет "state")
        {"invalid": "data"},  # Будет отфильтрован (нет "state")
    ]

    result = filter_by_state(transactions, "EXECUTED")
    assert len(result) == 1
    assert result[0]["state"] == "EXECUTED"


def test_sort_by_date_with_empty() -> None:
    """Тест сортировки с некорректными данными (пустые словари и None отфильтровываются)."""
    transactions: List[Dict[str, Any]] = [
        {"date": "2023-01-01"},
        {},  # Будет отфильтрован (нет "date")
        {"invalid": "data"},  # Будет отфильтрован (нет "date")
    ]

    result = sort_by_date(transactions)
    assert len(result) == 1
    assert "date" in result[0]
