from src.masks import get_mask_card_number, get_mask_account
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
from src.widget import format_date

def main():
    # Пример данных для демонстрации
    transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 7000792289606361",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "CANCELED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }
    ]

    print("=== Демонстрация работы всех функций проекта ===")

    # 1. Маскировка карт и счетов
    print("\n1. Маскировка номеров:")
    card = "7000792289606361"
    account = "73654108430135874305"
    print(f"Карта {card} -> {get_mask_card_number(card)}")
    print(f"Счет {account} -> {get_mask_account(account)}")

    # 2. Фильтрация и сортировка транзакций
    print("\n2. Обработка транзакций:")
    print("Исполненные транзакции:")
    for t in filter_by_state(transactions, "EXECUTED"):
        print(f"- {t['description']} ({t['date']})")

    print("\nОтсортированные по дате:")
    for t in sort_by_date(transactions):
        print(f"- {t['date']}: {t['description']}")

    # 3. Генераторы
    print("\n3. Работа генераторов:")
    print("Транзакции в USD:")
    for t in filter_by_currency(transactions, "USD"):
        print(f"- {t['description']}: {t['operationAmount']['amount']} {t['operationAmount']['currency']['code']}")

    print("\nОписания транзакций:")
    for desc in transaction_descriptions(transactions):
        print(f"- {desc}")

    print("\nГенерация номеров карт (1-5):")
    for card_num in card_number_generator(1, 5):
        print(card_num)

    # 4. Форматирование даты
    print("\n4. Форматирование даты:")
    print("2018-06-30T02:08:58.425572 ->", format_date("2018-06-30T02:08:58.425572"))

if __name__ == "__main__":
    main()
