import pytest
from src.widget import format_date, mask_account_card


@pytest.mark.parametrize("input_date,expected", [
    ("2018-07-11T02:26:18.671407", "11.07.2018"),
    ("2019-04-04T23:20:05.206878", "04.04.2019"),
    ("2020-12-31T01:00:00.000000", "31.12.2020"),
    ("2021-01-01T00:00:00.000000", "01.01.2021")
])
def test_format_date(input_date: str, expected: str) -> None:
    """Тестирование корректного форматирования даты из ISO формата в DD.MM.YYYY.

    Args:
        input_date: Строка с датой в ISO формате (YYYY-MM-DDTHH:MM:SS.mmmmmm)
        expected: Ожидаемый результат в формате DD.MM.YYYY

    Проверяет, что функция format_date правильно преобразует:
    - Разные корректные даты
    - Сохраняет правильный формат вывода
    """
    assert format_date(input_date) == expected


def test_format_date_errors() -> None:
    """Тестирование обработки некорректных входных данных функцией format_date.

    Проверяет, что функция вызывает ValueError для:
    - Пустой строки
    - Строки с некорректным форматом даты
    """
    with pytest.raises(ValueError):
        format_date("")
    with pytest.raises(ValueError):
        format_date("invalid")


@pytest.mark.parametrize("input_account,expected", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("7000792289606361", "7000 79** **** 6361"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ("", ""),
    ("Not a card", "Not a card")
])
def test_mask_account_card_valid(input_account: str, expected: str) -> None:
    """Тестирование корректной работы функции mask_account_card с валидными данными.

    Args:
        input_account: Входная строка с информацией о карте/счете
        expected: Ожидаемый результат после маскировки

    Проверяет:
    - Маскировку карт с указанием типа (Visa, Mastercard и т.д.)
    - Маскировку номера карты без указания типа
    - Маскировку счетов
    - Обработку пустой строки
    - Обработку строк, не содержащих номер карты/счета
    """
    assert mask_account_card(input_account) == expected


def test_mask_account_card_invalid_input() -> None:
    """Тестирование обработки некорректных входных данных функцией mask_account_card.

    Проверяет, что функция корректно обрабатывает:
    - None
    - Числовые значения
    - Списки строк

    Для всех этих случаев ожидается возврат строки "Некорректные данные".
    """
    assert mask_account_card(None) == "Некорректные данные"
    assert mask_account_card(123456) == "Некорректные данные"
    assert mask_account_card(["Visa", "1234"]) == "Некорректные данные"
