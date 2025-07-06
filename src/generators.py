from typing import Iterator, Dict, List, Any


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    """
    Фильтрует транзакции по заданной валюте.

    Args:
        transactions: Список транзакций
        currency: Код валюты для фильтрации (например, "USD")

    Yields:
        Транзакции с указанной валютой
    """
    for transaction in transactions:
        try:
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction
        except (KeyError, TypeError):
            continue


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """
    Генерирует описания транзакций.

    Args:
        transactions: Список транзакций

    Yields:
        Описание каждой транзакции
    """
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генерирует номера карт в заданном диапазоне.

    Args:
        start: Начальный номер (1-9999999999999999)
        end: Конечный номер (должен быть >= start)

    Yields:
        Номера карт в формате XXXX XXXX XXXX XXXX
    """
    for number in range(start, end + 1):
        yield f"{number:016d}"[:4] + " " + f"{number:016d}"[4:8] + " " + \
            f"{number:016d}"[8:12] + " " + f"{number:016d}"[12:16]
