import pytest
from typing import List, Dict, Union
from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_transactions() -> List[Dict[str, Union[str, int]]]:
    """Фикстура возвращает тестовый набор транзакций.

    Returns:
        Список словарей с транзакциями, где:
        - id (int): идентификатор транзакции
        - state (str): статус транзакции
        - date (str): дата в ISO формате
    """
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01T00:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2024-01-01T00:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2022-01-01T00:00:00"},
        {"id": 4, "state": "PENDING", "date": "2021-01-01T00:00:00"}
    ]


@pytest.fixture
def executed_transactions() -> List[Dict[str, Union[str, int]]]:
    """Фикстура возвращает только выполненные транзакции."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01T00:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2022-01-01T00:00:00"}
    ]


@pytest.fixture
def canceled_transactions() -> List[Dict[str, Union[str, int]]]:
    """Фикстура возвращает только отмененные транзакции."""
    return [{"id": 2, "state": "CANCELED", "date": "2024-01-01T00:00:00"}]


# Остальные функции остаются без изменений, как в предыдущем исправлении
def test_filter_by_state_default(
        sample_transactions: List[Dict[str, Union[str, int]]],
        executed_transactions: List[Dict[str, Union[str, int]]]
) -> None:
    """Тестирует фильтрацию по умолчанию (EXECUTED)."""
    result = filter_by_state(sample_transactions)
    assert result == executed_transactions


def test_filter_by_state_executed(
        sample_transactions: List[Dict[str, Union[str, int]]],
        executed_transactions: List[Dict[str, Union[str, int]]]
) -> None:
    """Тестирует явную фильтрацию по статусу EXECUTED."""
    result = filter_by_state(sample_transactions, "EXECUTED")
    assert result == executed_transactions


def test_filter_by_state_canceled(
        sample_transactions: List[Dict[str, Union[str, int]]],
        canceled_transactions: List[Dict[str, Union[str, int]]]
) -> None:
    """Тестирует фильтрацию по статусу CANCELED."""
    result = filter_by_state(sample_transactions, "CANCELED")
    assert result == canceled_transactions


def test_sort_by_date_descending(sample_transactions: List[Dict[str, Union[str, int]]]) -> None:
    """Тестирует сортировку по убыванию даты (новые сначала)."""
    result = sort_by_date(sample_transactions)
    assert [t["date"] for t in result] == [
        "2024-01-01T00:00:00",
        "2023-01-01T00:00:00",
        "2022-01-01T00:00:00",
        "2021-01-01T00:00:00"
    ]


def test_sort_by_date_ascending(sample_transactions: List[Dict[str, Union[str, int]]]) -> None:
    """Тестирует сортировку по возрастанию даты (старые сначала)."""
    result = sort_by_date(sample_transactions, reverse=False)
    assert [t["date"] for t in result] == [
        "2021-01-01T00:00:00",
        "2022-01-01T00:00:00",
        "2023-01-01T00:00:00",
        "2024-01-01T00:00:00"
    ]
