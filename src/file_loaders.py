"""Модуль для загрузки транзакций из CSV и Excel."""
import pandas as pd
import logging

logger = logging.getLogger(__name__)


def load_transactions_csv(filepath: str) -> list:
    """
    Считывает финансовые операции из CSV-файла.

    Args:
        filepath: Путь к файлу.

    Returns:
        Список словарей с транзакциями.
    """
    logger.info(f"Загрузка из CSV: {filepath}")
    try:
        df = pd.read_csv(filepath)
        return df.to_dict(orient="records")
    except Exception as e:
        logger.error(f"Ошибка CSV: {e}")
        return []


def load_transactions_excel(filepath: str) -> list:
    """
    Считывает финансовые операции из Excel-файла.

    Args:
        filepath: Путь к файлу.

    Returns:
        Список словарей с транзакциями.
    """
    logger.info(f"Загрузка из Excel: {filepath}")
    try:
        df = pd.read_excel(filepath)
        return df.to_dict(orient="records")
    except Exception as e:
        logger.error(f"Ошибка Excel: {e}")
        return []
