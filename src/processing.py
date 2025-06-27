from datetime import datetime
from typing import List, Dict


def filter_by_state(transactions: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Фильтрует транзакции по указанному статусу.

    Args:
        transactions: Список словарей с транзакциями
        state: Статус для фильтрации (по умолчанию 'EXECUTED')

    Returns:
        Отфильтрованный список транзакций.
    """
    return [t for t in transactions if t.get("state") == state]


def sort_by_date(transactions: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует транзакции по дате.

    Args:
        transactions: Список словарей с транзакциями
        reverse: Если True - сортировка по убыванию (новые сначала)

    Returns:
        Отсортированный список транзакций
    """
    return sorted(
        transactions,
        key=lambda x: datetime.fromisoformat(x["date"]),
        reverse=reverse
    )
