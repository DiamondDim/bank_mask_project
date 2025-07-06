from typing import List, Dict, Any


def filter_by_state(
        transactions: List[Dict[str, Any]], state: str
) -> List[Dict[str, Any]]:
    """
    Фильтрует список транзакций по заданному статусу.
    Игнорирует None и словари без поля 'state'.

    :param transactions: Список транзакций (словарей)
    :param state: Статус для фильтрации ("EXECUTED", "CANCELED" и т.д.)
    :return: Отфильтрованный список транзакций
    """
    return [
        t for t in transactions
        if isinstance(t, dict) and t.get("state") == state
    ]


def sort_by_date(transactions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Сортирует транзакции по дате (от новых к старым).
    Игнорирует None и словари без поля 'date'.

    :param transactions: Список транзакций (словарей)
    :return: Отсортированный список транзакций
    """
    valid_transactions = [
        t for t in transactions
        if isinstance(t, dict) and "date" in t
    ]
    return sorted(valid_transactions, key=lambda x: x["date"], reverse=True)
