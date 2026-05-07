import json
import logging
import os
from pathlib import Path

# Создаём папку logs, если нет
os.makedirs("logs", exist_ok=True)

# Создаём отдельный логгер для модуля
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Настраиваем FileHandler с перезаписью (mode="w")
file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# Формат: время | модуль | уровень | сообщение
formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")
file_handler.setFormatter(formatter)

# Подключаем handler к логгеру
logger.addHandler(file_handler)


def load_operations(filepath: str) -> list:
    """
    Читает JSON-файл с финансовыми операциями.
    Возвращает список словарей или пустой список при ошибке.
    """
    logger.info(f"Начинаю загрузку из: {filepath}")

    try:
        path = Path(filepath)
        if not path.exists():
            logger.warning(f"Файл не найден: {filepath}")
            return []

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            logger.error("Файл содержит не список операций!")
            return []

        logger.info(f"Успешно загружено {len(data)} операций.")
        return data

    except json.JSONDecodeError as e:
        logger.error(f"Ошибка парсинга JSON: {e}")
        return []
    except Exception as e:
        logger.error(f"Неизвестная ошибка: {e}")
        return []

