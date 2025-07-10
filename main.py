import random
from typing import Any, Dict

from src.decorators import log
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.masks import mask_account_number, mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import format_date


@log()
def calculate_interest(amount: float, rate: float, years: int) -> float:
    """Рассчитывает сумму с учетом процентов (демонстрация логирования)"""
    if amount <= 0:
        raise ValueError("Сумма должна быть положительной")
    return amount * (1 + rate / 100) ** years


@log(filename="bank_operations.log")
def process_transaction(transaction: Dict[str, Any]) -> str:
    """Обрабатывает транзакцию с логированием в файл"""
    if not transaction.get("id"):
        raise ValueError("Транзакция не содержит ID")

    amount = transaction.get("amount", 0)
    currency = transaction.get("currency", "USD")

    if random.random() < 0.2:
        raise RuntimeError("Случайная ошибка обработки транзакции")

    return f"Транзакция {transaction['id']} на сумму {amount} {currency} обработана"


def demonstrate_logging() -> None:
    """Демонстрация работы декоратора log"""
    print("\n=== Демонстрация логирования ===")

    # Логирование в консоль
    try:
        interest = calculate_interest(10000, 5, 3)
        print(f"Начисленные проценты: {interest:.2f}")
    except ValueError as e:
        print(f"Ошибка: {e}")

    # Логирование в файл
    sample_transaction = {"id": "123456", "amount": 1500.75, "currency": "RUB", "description": "Покупка в магазине"}

    try:
        result = process_transaction(sample_transaction)
        print(result)
    except Exception as e:
        print(f"Ошибка обработки транзакции: {e}")


def main() -> None:
    """Основная функция для демонстрации возможностей проекта"""
    # Пример данных для демонстрации
    transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 7000792289606361",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "CANCELED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]

    print("=== Демонстрация работы всех функций проекта ===")

    # 1. Маскировка карт и счетов
    print("\n1. Маскировка номеров:")
    card = "7000792289606361"
    account = "73654108430135874305"
    print(f"Карта {card} -> {mask_card_number(card)}")
    print(f"Счет {account} -> {mask_account_number(account)}")

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

    # 5. Демонстрация логирования
    demonstrate_logging()

    print("\nПроверьте файл 'bank_operations.log' для просмотра записанных логов")


if __name__ == "__main__":
    main()
