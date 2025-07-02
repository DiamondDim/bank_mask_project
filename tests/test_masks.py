import pytest
from typing import List, Tuple
from src.masks import get_mask_card_number, get_mask_account


@pytest.fixture
def valid_card_numbers() -> List[Tuple[str, str]]:
    """Фикстура возвращает валидные номера карт и ожидаемые результаты маскировки."""
    return [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1234567890123456", "1234 56** **** 3456")
    ]


@pytest.fixture
def valid_account_numbers() -> List[Tuple[str, str]]:
    """Фикстура возвращает валидные номера счетов и ожидаемые результаты маскировки."""
    return [
        ("73654108430135874305", "**4305"),
        ("12345678901234567890", "**7890")
    ]


@pytest.fixture
def invalid_inputs() -> List[Tuple[str, str]]:
    """Фикстура возвращает невалидные входные данные и описания ошибок."""
    return [
        ("123", "Слишком короткий номер"),
        ("12a45", "Содержит буквы"),
        ("123456789012345", "15 цифр")
    ]


def test_mask_card_valid(valid_card_numbers: List[Tuple[str, str]]) -> None:
    """Тестирует маскировку валидных номеров карт."""
    for number, expected in valid_card_numbers:
        assert get_mask_card_number(number) == expected


def test_mask_card_empty() -> None:
    """Тестирует обработку пустой строки для номера карты."""
    assert get_mask_card_number("") == ""


def test_mask_card_invalid(invalid_inputs: List[Tuple[str, str]]) -> None:
    """Тестирует обработку невалидных номеров карт."""
    for number, _ in invalid_inputs[:2]:
        with pytest.raises(ValueError):
            get_mask_card_number(number)


def test_mask_account_valid(valid_account_numbers: List[Tuple[str, str]]) -> None:
    """Тестирует маскировку валидных номеров счетов."""
    for number, expected in valid_account_numbers:
        assert get_mask_account(number) == expected


def test_mask_account_empty() -> None:
    """Тестирует обработку пустой строки для номера счета."""
    assert get_mask_account("") == ""


def test_mask_account_invalid(invalid_inputs: List[Tuple[str, str]]) -> None:
    """Тестирует обработку невалидных номеров счетов."""
    for number, _ in invalid_inputs[:2]:
        with pytest.raises(ValueError):
            get_mask_account(number)


@pytest.mark.parametrize(
    "input_data,expected,is_valid",
    [
        ("", "", True),
        ("1234", "**1234", True),
        ("123", None, False),
        ("1234567890123456", "1234 56** **** 3456", True),
        ("12a34", None, False)
    ]
)
def test_masks_combined(
        input_data: str,
        expected: str,
        is_valid: bool
) -> None:
    """Комбинированный тест для проверки граничных случаев.

    Args:
        input_data: Входные данные для тестирования
        expected: Ожидаемый результат для валидных данных
        is_valid: Флаг валидности входных данных
    """
    if not is_valid:
        with pytest.raises(ValueError):
            if len(input_data) <= 4:
                get_mask_account(input_data)
            else:
                get_mask_card_number(input_data)
    else:
        if len(input_data) <= 4 and input_data:
            assert get_mask_account(input_data) == expected
        elif input_data:
            assert get_mask_card_number(input_data) == expected
