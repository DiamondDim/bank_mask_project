import pytest
from src.widget import format_date, mask_account_card


# Тесты для format_date (оставляем без изменений)
@pytest.mark.parametrize(
    "input_date, expected_output",
    [
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("2019-04-04T23:20:05.206878", "04.04.2019"),
        ("2020-12-31T01:00:00.000000", "31.12.2020"),
        ("2021-01-01T00:00:00.000000", "01.01.2021"),
    ],
)
def test_format_date(input_date: str, expected_output: str) -> None:
    assert format_date(input_date) == expected_output


def test_format_date_with_empty_string() -> None:
    with pytest.raises(ValueError):
        format_date("")


def test_format_date_with_invalid_format() -> None:
    with pytest.raises(ValueError):
        format_date("2021/01/01")


# Тесты для mask_account_card
@pytest.mark.parametrize(
    "input_account, expected_output",
    [
        # Карты
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("МИР 1234567890123456", "МИР 1234 56** **** 3456"),
        ("7000792289606361", "7000 79** **** 6361"),  # Только номер

        # Счета
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 1234567890123456", "Счет **3456"),
        ("Счет 9876543210", "Счет **3210"),

        # Краевые случаи
        ("", ""),
        ("Счет", "Счет"),
        ("Visa", "Visa"),
        ("12345678", "12345678"),
        ("Not a card or account", "Not a card or account"),
    ],
)
def test_mask_account_card_valid(input_account: str, expected_output: str) -> None:
    assert mask_account_card(input_account) == expected_output


# Отдельный тест для некорректных типов
def test_mask_account_card_invalid_input() -> None:
    assert mask_account_card(None) == "Некорректные данные"
    assert mask_account_card(123456) == "Некорректные данные"
    assert mask_account_card(["Visa", "1234123412341234"]) == "Некорректные данные"
