from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.masks import mask_account_number, mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import format_date
from decorators import log
import random


def main() -> None:
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


@log()
def calculate_interest(amount: float, rate: float, years: int) -> float:
    """Рассчитывает сумму с учетом процентов"""
    return amount * (1 + rate / 100) ** years


@log(filename="bank_operations.log")
def transfer_funds(from_account: str, to_account: str, amount: float) -> str:
    """Имитирует перевод средств между счетами"""
    if amount <= 0:
        raise ValueError("Сумма перевода должна быть положительной")
    if len(from_account) != 20 or len(to_account) != 20:
        raise ValueError("Номер счета должен содержать 20 цифр")

    # Имитация случайной ошибки (для демонстрации)
    if random.random() < 0.3:
        raise RuntimeError("Ошибка соединения с банковским сервером")

    return f"Перевод {amount:.2f}₽ с {from_account} на {to_account} выполнен успешно"


@log()
def validate_account(account_number: str) -> bool:
    """Проверяет валидность номера счета"""
    return account_number.isdigit() and len(account_number) == 20


def demonstrate_logging() -> None:
    """Демонстрация работы декоратора log"""
    print("\n=== Демонстрация логирования в консоль ===")

    # Успешный вызов
    interest = calculate_interest(100000, 7.5, 5)
    print(f"Результат расчета процентов: {interest:.2f}₽")

    # Вызов с ошибкой
    try:
        calculate_interest(-10000, 5, 2)
    except ValueError as e:
        print(f"Ожидаемая ошибка: {e}")

    # Проверка счета
    is_valid = validate_account("12345678901234567890")
    print(f"Счет валиден: {is_valid}")

    print("\n=== Демонстрация логирования в файл ===")
    print("Логи будут записаны в файл 'bank_operations.log'")

    # Успешный перевод
    try:
        result = transfer_funds("12345678901234567890", "09876543210987654321", 15000.50)
        print(result)
    except Exception as e:
        print(f"Ошибка перевода: {e}")

    # Перевод с ошибкой
    try:
        transfer_funds("123", "09876543210987654321", 500)
    except Exception as e:
        print(f"Ожидаемая ошибка: {e}")


if __name__ == "__main__":
    main()
    print("Демонстрация работы декоратора логирования")
    demonstrate_logging()
    print("\nПроверьте файл 'bank_operations.log' для просмотра записанных логов")