import pytest
from typing import Dict, List, Any, Union
from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_transactions() -> List[Union[Dict[str, Any], None]]:
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2023-01-01T00:00:00"
        },
        {
            "id": 2,
            "state": "CANCELED",
            "date": "2023-02-01T00:00:00"
        },
        {},  # Пустой словарь
        None,  # None-элемент
    ]


def test_filter_by_state_with_empty() -> None:
    """Тестирует обработку пустых и некорректных транзакций"""
    transactions = [
        {"state": "EXECUTED"},
        {},  # Пустой словарь
        {"invalid": "data"},  # Нет поля state
        None  # None
    ]

    result = filter_by_state(transactions, "EXECUTED")
    assert len(result) == 1
    assert result[0]["state"] == "EXECUTED"


def test_sort_by_date_with_empty() -> None:
    """Тестирует сортировку с пустыми данными"""
    transactions = [
        {"date": "2023-01-01"},
        {},  # Пустой словарь
        {"invalid": "data"},  # Нет поля date
        None  # None
    ]

    result = sort_by_date(transactions)
    assert len(result) == 1
    assert "date" in result[0]
