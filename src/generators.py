from typing import Iterator, Dict, Any, List


def filter_by_currency(transactions: List[Dict[str, Any]], currency_code: str) -> Iterator[Dict[str, Any]]:
    """
    Генератор, фильтрующий транзакции по коду валюты.

    Args:
        transactions: Список транзакций
        currency_code: Код валюты (например, "USD")

    Yields:
        Транзакции с указанной валютой
    """
    for transaction in transactions:
        op_amount = transaction.get("operationAmount", {})
        curr = op_amount.get("currency", {})
        if curr.get("code") == currency_code:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """
    Генератор описаний транзакций.

    Args:
        transactions: Список транзакций

    Yields:
        Описание каждой транзакции
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генератор номеров карт в заданном диапазоне.

    Args:
        start: Начальный номер (1..9999999999999999)
        end: Конечный номер (>=start)

    Yields:
        Номера карт в формате "XXXX XXXX XXXX XXXX"
    """
    for num in range(start, end + 1):
        yield f"{num:016d}"[:4] + " " + f"{num:016d}"[4:8] + " " + f"{num:016d}"[8:12] + " " + f"{num:016d}"[12:16]
