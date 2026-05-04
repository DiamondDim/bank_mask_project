import json
from pathlib import Path


def load_operations(filepath: str) -> list:
    """
    Читает JSON-файл с финансовыми операциями.

    Args:
        filepath: Путь к JSON-файлу.

    Returns:
        Список словарей с данными транзакций.
        Если файл не найден, пуст или содержит не список — возвращает [].
    """
    try:
        path = Path(filepath)
        if not path.exists():
            return []

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Проверяем, что внутри именно список
        if not isinstance(data, list):
            return []

        return data

    except (json.JSONDecodeError, Exception):
        # Если файл битый или другая ошибка чтения
        return []
