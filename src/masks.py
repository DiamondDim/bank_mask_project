import logging
import os

# Создаём папку logs, если нет
os.makedirs("logs", exist_ok=True)

# Логгер для модуля masks
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты в формате XXXX XX** **** XXXX.
    """
    logger.info(f"Маскирую номер карты: {card_number}")

    if len(card_number) != 16 or not card_number.isdigit():
        logger.error(f"Некорректный номер карты: {card_number}")
        raise ValueError("Номер карты должен содержать 16 цифр")

    masked = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    logger.info(f"Успешно замаскирован: {masked}")
    return masked


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счёта в формате **XXXX.
    """
    logger.info(f"Маскирую номер счёта: {account_number}")

    if len(account_number) < 4 or not account_number.isdigit():
        logger.error(f"Некорректный номер счёта: {account_number}")
        raise ValueError("Номер счёта должен содержать минимум 4 цифры")

    masked = f"**{account_number[-4:]}"
    logger.info(f"Успешно замаскирован: {masked}")
    return masked

