import pytest
from typing import List, Dict, Any
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def sample_transactions() -> List[Dict[str, Any]]:
    """
    Фикстура предоставляет тестовые данные транзакций.

    Returns:
        Список тестовых транзакций в формате:
        [
            {
                "id": int,
                "operationAmount": {
                    "currency": {"code": str}
                },
                "description": str
            },
            ...
        ]
    """
    return [
        {
            "id": 1,
            "operationAmount": {
                "currency": {"code": "USD"}
            },
            "description": "Transaction 1"
        },
        {
            "id": 2,
            "operationAmount": {
                "currency": {"code": "EUR"}
            },
            "description": "Transaction 2"
        },
        {
            "id": 3,
            "operationAmount": {
                "currency": {"code": "USD"}
            },
            "description": "Transaction 3"
        }
    ]


def test_filter_by_currency(sample_transactions: List[Dict[str, Any]]) -> None:
    """
    Тестирует фильтрацию транзакций по валюте.

    Проверяет:
    1. Корректность фильтрации транзакций
    2. Порядок возвращаемых транзакций
    3. Завершение итератора при отсутствии данных

    Args:
        sample_transactions: Фикстура с тестовыми данными
    """
    usd_transactions = filter_by_currency(sample_transactions, "USD")

    # Проверка первой USD-транзакции
    first_transaction = next(usd_transactions)
    assert first_transaction["id"] == 1
    assert first_transaction["operationAmount"]["currency"]["code"] == "USD"

    # Проверка второй USD-транзакции
    second_transaction = next(usd_transactions)
    assert second_transaction["id"] == 3

    # Проверка завершения итератора
    with pytest.raises(StopIteration):
        next(usd_transactions)


def test_transaction_descriptions(sample_transactions: List[Dict[str, Any]]) -> None:
    """
    Тестирует генератор описаний транзакций.

    Проверяет:
    1. Корректность возвращаемых описаний
    2. Порядок следования описаний

    Args:
        sample_transactions: Фикстура с тестовыми данными
    """
    descriptions = transaction_descriptions(sample_transactions)

    assert next(descriptions) == "Transaction 1"
    assert next(descriptions) == "Transaction 2"
    assert next(descriptions) == "Transaction 3"

    # Проверка завершения итератора
    with pytest.raises(StopIteration):
        next(descriptions)


@pytest.mark.parametrize(
    "start,end,expected",
    [
        (1, 1, ["0000 0000 0000 0001"]),
        (1, 3, [
            "0000 0000 0000 0001",
            "0000 0000 0000 0002",
            "0000 0000 0000 0003"
        ]),
    ],
    ids=["single_card", "multiple_cards"]
)
def test_card_number_generator(start: int, end: int, expected: List[str]) -> None:
    """
    Параметризованный тест генератора номеров карт.

    Проверяет:
    1. Корректность генерации номеров
    2. Форматирование вывода
    3. Обработку диапазонов

    Args:
        start: Начальный номер диапазона
        end: Конечный номер диапазона
        expected: Ожидаемый список номеров карт
    """
    result = list(card_number_generator(start, end))
    assert result == expected
    assert all(len(num) == 19 for num in result)  # Проверка формата
