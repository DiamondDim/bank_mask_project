import requests

api_key = "mL3TtjvEW3CKaDVSAQsu0usJwjdyTdWT"

# Пробуем Вариант A (access_key)
url_a = f"https://api.apilayer.com/exchangerates_data/latest?access_key={api_key}&base=USD&symbols=RUB"
print("🔍 Тест Вариант A (access_key):")
try:
    resp = requests.get(url_a, timeout=5)
    print(f"Статус: {resp.status_code}")
    print(f"Ответ: {resp.text[:200]}")
except Exception as e:
    print(f"Ошибка: {e}")

print("\n" + "="*50 + "\n")

# Пробуем Вариант B (apikey в заголовке)
url_b = "https://api.apilayer.com/api/v2/latest"
headers = {"apikey": api_key}
params = {"base": "USD", "symbols": "RUB"}
print("🔍 Тест Вариант B (apikey в заголовке):")
try:
    resp = requests.get(url_b, headers=headers, params=params, timeout=5)
    print(f"Статус: {resp.status_code}")
    print(f"Ответ: {resp.text[:200]}")
except Exception as e:
    print(f"Ошибка: {e}")

