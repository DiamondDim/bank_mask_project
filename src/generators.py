from typing import Iterator, Dict, List, Any, Optional


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    """
    Фильтрует транзакции по указанной валюте.

    Args:
        transactions: Список транзакций (каждая - словарь)
        currency: Код валюты для фильтрации (например, "USD")

    Yields:
        Словари транзакций с указанной валютой

    Examples:
        >>> list(filter_by_currency([{"operationAmount": {"currency": {"code": "USD"}}}], "USD"))
        [{'operationAmount': {'currency': {'code': 'USD'}}}]
    """
    for transaction in transactions:
        if not isinstance(transaction, dict):
            continue

        try:
            op_amount = transaction.get('operationAmount', {})
            if isinstance(op_amount, dict) and op_amount.get('currency', {}).get('code') == currency:
                yield transaction
        except (AttributeError, TypeError):
            continue


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """
    Генерирует описания транзакций.

    Args:
        transactions: Список транзакций

    Yields:
        Описание каждой транзакции (str)

    Examples:
        >>> list(transaction_descriptions([{"description": "Payment"}]))
        ['Payment']
    """
    for transaction in transactions:
        yield str(transaction.get('description', '')) if isinstance(transaction, dict) else ''


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генерирует номера карт в заданном диапазоне.

    Args:
        start: Начальный номер (>=1)
        end: Конечный номер (>=start)

    Yields:
        Номера карт в формате "XXXX XXXX XXXX XXXX"

    Examples:
        >>> list(card_number_generator(1, 2))
        ['0000 0000 0000 0001', '0000 0000 0000 0002']
    """
    if start < 1 or end < start:
        raise ValueError("Некорректный диапазон")

    for number in range(start, end + 1):
        num_str = f"{number:016d}"
        yield f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:16]}"
