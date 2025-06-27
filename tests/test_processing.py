from typing import List, Dict, Union
from src.processing import filter_by_state, sort_by_date

SAMPLE_DATA: List[Dict[str, Union[str, int]]] = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
]


def test_filter_by_state() -> None:
    """Тестирование фильтрации транзакций по статусу."""
    # Тестируем фильтрацию по EXECUTED
    result: List[Dict[str, Union[str, int]]] = filter_by_state(SAMPLE_DATA)
    assert len(result) == 2
    assert all(t["state"] == "EXECUTED" for t in result)

    # Тестируем фильтрацию по CANCELED
    result = filter_by_state(SAMPLE_DATA, "CANCELED")
    assert len(result) == 2
    assert all(t["state"] == "CANCELED" for t in result)


def test_sort_by_date() -> None:
    """Тестирование сортировки транзакций по дате."""
    # Тестируем сортировку по убыванию (по умолчанию)
    result: List[Dict[str, Union[str, int]]] = sort_by_date(SAMPLE_DATA)
    assert result[0]["date"] == "2019-07-03T18:35:29.512364"
    assert result[-1]["date"] == "2018-06-30T02:08:58.425572"

    # Тестируем сортировку по возрастанию
    result = sort_by_date(SAMPLE_DATA, reverse=False)
    assert result[0]["date"] == "2018-06-30T02:08:58.425572"
    assert result[-1]["date"] == "2019-07-03T18:35:29.512364"
