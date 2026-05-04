from src.utils import load_operations
from src.external_api import convert_currency

data = load_operations("data/operations.json")

# Берём первые 3 операции для проверки
for tx in data[:3]:
    rub_amount = convert_currency(tx)
    currency = tx.get("operationAmount", {}).get("currency", {}).get("name", "RUB")
    print(f" {currency} {tx['operationAmount']['amount']} → {rub_amount} RUB")

