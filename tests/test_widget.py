import pytest
from src.widget import format_date, mask_account_card


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
    """Тестирование функции format_date с валидными входными данными"""
    assert format_date(input_date) == expected_output


def test_format_date_with_empty_string() -> None:
    """Тестирование обработки пустой строки"""
    with pytest.raises(ValueError, match="Некорректная дата"):
        format_date("")


def test_format_date_with_invalid_format() -> None:
    """Тестирование обработки неверного формата даты"""
    with pytest.raises(ValueError, match="Некорректная дата"):
        format_date("2021/01/01")


def test_format_date_with_none() -> None:
    """Тестирование обработки None"""
    with pytest.raises(ValueError, match="Некорректная дата"):
        format_date(None)


def test_format_date_with_number() -> None:
    """Тестирование обработки числового ввода"""
    with pytest.raises(ValueError, match="Некорректная дата"):
        format_date(123456)
