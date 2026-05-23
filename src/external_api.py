import os

import requests
from dotenv import load_dotenv

# Загружаем переменные из .env один раз при импорте
load_dotenv()


def convert_currency(transaction: dict) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    Args:
        transaction: Словарь с данными операции.

    Returns:
        Сумма в рублях (float). При ошибке возвращает исходную сумму.
    """
    amount_data = transaction.get("operationAmount", {})
    amount = float(amount_data.get("amount", 0))
    currency = amount_data.get("currency", {}).get("name", "RUB")

    if currency == "RUB":
        return amount

    if currency in ["USD", "EUR"]:
        api_key = os.getenv("EXCHANGE_API_KEY")
        if not api_key:
            print("EXCHANGE_API_KEY не найден в .env")
            return amount

        try:
            url = "https://api.apilayer.com/exchangerates_data/latest"
            headers = {"apikey": api_key}
            params = {"base": currency, "symbols": "RUB"}

            response = requests.get(url, headers=headers, params=params, timeout=10)
            response.raise_for_status()  # Вызовет ошибку при 4xx/5xx

            data = response.json()
            rate = data.get("rates", {}).get("RUB")

            if rate:
                return round(amount * rate, 2)

        except requests.exceptions.RequestException as e:
            print(f"Ошибка запроса к API: {e}")

    return amount
