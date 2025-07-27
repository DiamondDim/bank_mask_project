from typing import Any, Dict, List


def filter_by_state(transactions: List[Dict[str, Any]], state: str) -> List[Dict[str, Any]]:
    """
    Фильтрует транзакции по указанному статусу.

    Args:
        transactions: Список транзакций
        state: Статус для фильтрации ("EXECUTED", "CANCELED" и т.д.)

    Returns:
        Отфильтрованный список транзакций

    Examples:
        >>> filter_by_state([{"state": "EXECUTED"}], "EXECUTED")
        [{'state': 'EXECUTED'}]
    """
    return [t for t in transactions if isinstance(t, dict) and t.get("state") == state]


def sort_by_date(transactions: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует транзакции по дате.

    Args:
        transactions: Список транзакций
        reverse: Сортировка по убыванию (True) или возрастанию (False)

    Returns:
        Отсортированный список транзакций

    Examples:
        >>> sort_by_date([{"date": "2023-01-01"}, {"date": "2023-01-02"}])
        [{'date': '2023-01-02'}, {'date': '2023-01-01'}]
    """

    def get_date(transaction: Dict[str, Any]) -> str:
        date = transaction.get("date", "")
        return str(date)

    return sorted([t for t in transactions if "date" in t], key=lambda x: x["date"], reverse=reverse)
