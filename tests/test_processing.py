"""Тесты к новым функциональностям проекта."""
import pytest  # noqa: F401

from src.processing import process_bank_operations, process_bank_search

SAMPLE_DATA = [
    {"description": "Перевод клиенту", "state": "EXECUTED", "date": "01.01.2023", "operationAmount": {"currency": {"name": "RUB"}}},
    {"description": "Оплата услуг ЖКХ", "state": "CANCELED", "date": "02.01.2023", "operationAmount": {"currency": {"name": "USD"}}},
    {"description": "Перевод организации", "state": "EXECUTED", "date": "03.01.2023", "operationAmount": {"currency": {"name": "RUB"}}},
]


def test_process_bank_search_found():
    assert len(process_bank_search(SAMPLE_DATA, "Перевод")) == 2


def test_process_bank_search_case_insensitive():
    assert len(process_bank_search(SAMPLE_DATA, "перевод")) == 2


def test_process_bank_search_empty():
    assert process_bank_search(SAMPLE_DATA, "Кредит") == []


def test_process_bank_operations_count():
    result = process_bank_operations(SAMPLE_DATA, ["Перевод", "Оплата"])
    assert result == {"Перевод": 2, "Оплата": 1}


def test_process_bank_operations_missing_category():
    result = process_bank_operations(SAMPLE_DATA, ["Перевод", "Зарплата"])
    assert result == {"Перевод": 2, "Зарплата": 0}
