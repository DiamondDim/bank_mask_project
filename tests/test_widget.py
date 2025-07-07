import pytest
from src.widget import mask_account_card, format_date

@pytest.mark.parametrize("input_str, expected", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Счет 73654108430135874305", "Счет **4305"),
], ids=["card", "account"])
def test_mask_account_card(input_str: str, expected: str) -> None:
    """Тестирует маскировку номеров карт и счетов"""
    assert mask_account_card(input_str) == expected

@pytest.mark.parametrize("date_str, expected", [
    ("2018-06-30T02:08:58.425572", "30.06.2018"),
    ("2023-10-01T00:00:00.000000", "01.10.2023"),
    ("invalid-date", "Некорректная дата"),
], ids=["valid", "valid2", "invalid"])
def test_format_date(date_str: str, expected: str) -> None:
    """Тестирует форматирование даты"""
    assert format_date(date_str) == expected


def test_format_date_invalid():
    """Тест обработки некорректных дат"""
    assert format_date("2023-13-01") == "Некорректная дата"  # Несуществующий месяц
    assert format_date("not-a-date") == "Некорректная дата"  # Полностью невалидный формат

def test_format_date_edge_cases():
     # Тест на некорректные даты
    assert format_date("invalid") == "Некорректная дата"
    assert format_date("2023-02-30") == "Некорректная дата"  # Несуществующая дата

