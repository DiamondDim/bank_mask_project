import pytest
from src.processing import filter_by_state, sort_by_date

@pytest.fixture
def sample_transactions():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01T00:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2024-01-01T00:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2022-01-01T00:00:00"},
        {"id": 4, "state": "PENDING", "date": "2021-01-01T00:00:00"}
    ]

@pytest.fixture
def executed_transactions():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01T00:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2022-01-01T00:00:00"}
    ]

@pytest.fixture
def canceled_transactions():
    return [{"id": 2, "state": "CANCELED", "date": "2024-01-01T00:00:00"}]

def test_filter_by_state_default(sample_transactions, executed_transactions):
    result = filter_by_state(sample_transactions)
    assert result == executed_transactions

def test_filter_by_state_executed(sample_transactions, executed_transactions):
    result = filter_by_state(sample_transactions, "EXECUTED")
    assert result == executed_transactions

def test_filter_by_state_canceled(sample_transactions, canceled_transactions):
    result = filter_by_state(sample_transactions, "CANCELED")
    assert result == canceled_transactions

def test_sort_by_date_descending(sample_transactions):
    result = sort_by_date(sample_transactions)
    dates = [t["date"] for t in result]
    assert dates == ["2024-01-01T00:00:00", "2023-01-01T00:00:00", 
                    "2022-01-01T00:00:00", "2021-01-01T00:00:00"]

def test_sort_by_date_ascending(sample_transactions):
    result = sort_by_date(sample_transactions, reverse=False)
    dates = [t["date"] for t in result]
    assert dates == ["2021-01-01T00:00:00", "2022-01-01T00:00:00",
                    "2023-01-01T00:00:00", "2024-01-01T00:00:00"]
