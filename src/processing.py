"""Обработка и фильтрация банковских операций."""
import logging
import re
from collections import Counter
from typing import Any, Dict, List

logger = logging.getLogger(__name__)


def process_bank_search(data: List[Dict[str, Any]], search: str) -> List[Dict[str, Any]]:
    """
    Ищет операции, содержащие заданную строку в поле description.
    Использует библиотеку re для поиска (регистронезависимый).
    """
    if not search:
        return data

    pattern = re.compile(re.escape(search), re.IGNORECASE)
    result = [tx for tx in data if pattern.search(tx.get("description", ""))]
    logger.info(f"Найдено {len(result)} операций по запросу '{search}'")
    return result


def process_bank_operations(data: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество банковских операций определённого типа.
    Использует Counter из collections для агрегации.
    """
    counts = Counter()
    for tx in data:
        desc = tx.get("description", "").lower()
        for cat in categories:
            if cat.lower() in desc:
                counts[cat] += 1
                break  # Одна операция учитывается только в первой совпавшей категории

    return {cat: counts.get(cat, 0) for cat in categories}


# #from datetime import datetime
# from typing import Dict, List
#
#
# def filter_by_state(transactions: List[Dict], state: str = "EXECUTED") -> List[Dict]:
#     """
#     Фильтрует транзакции по указанному статусу.
#
#     Args:
#         transactions: Список словарей с транзакциями
#         state: Статус для фильтрации (по умолчанию 'EXECUTED')
#
#     Returns:
#         Отфильтрованный список транзакций.
#     """
#     return [t for t in transactions if t.get("state") == state]
#
#
# def sort_by_date(transactions: List[Dict], reverse: bool = True) -> List[Dict]:
#     """
#     Сортирует транзакции по дате.
#
#     Args:
#         transactions: Список словарей с транзакциями
#         reverse: Если True - сортировка по убыванию (новые сначала)
#
#     Returns:
#         Отсортированный список транзакций
#     """
#     return sorted(transactions, key=lambda x: datetime.fromisoformat(x["date"]), reverse=reverse)
