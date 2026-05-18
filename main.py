"""Точка входа в проект. Реализует CLI для работы с транзакциями."""
import logging
from datetime import datetime
from typing import Any, Dict, List

from src.file_loaders import load_transactions_csv, load_transactions_excel
from src.processing import process_bank_search
from src.utils import load_operations

logging.basicConfig(level=logging.INFO, format="%(message)s")


def main() -> None:
    """Основная логика программы с пользовательским интерфейсом."""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input().strip()
    data: List[Dict[str, Any]] = []

    if choice == "1":
        data = load_operations("data/operations.json")
        print("Для обработки выбран JSON-файл.")
    elif choice == "2":
        data = load_transactions_csv("data/transactions.csv")
        print("Для обработки выбран CSV-файл.")
    elif choice == "3":
        data = load_transactions_excel("data/transactions_excel.xlsx")
        print("Для обработки выбран XLSX-файл.")
    else:
        print("Неверный выбор. Завершение программы.")
        return

    # 1. Фильтрация по статусу
    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print(f"Доступные для фильтровки статусы: {', '.join(valid_statuses)}")
        status_input = input().strip().upper()

        if status_input in valid_statuses:
            data = [tx for tx in data if str(tx.get("state", "")).upper() == status_input]
            print(f'Операции отфильтрованы по статусу "{status_input}"')
            break
        else:
            print(f'Статус операции "{status_input}" недоступен.')

    # 2. Сортировка по дате
    sort_q = input("Отсортировать операции по дате? (Да / Нет / Yes / No / Y / N)\n").strip().lower()
    if sort_q in ("да", "yes", "y"):
        direction = input("Отсортировать по возрастанию или по убыванию? (по возрастанию / по убыванию)\n").strip().lower()
        reverse = "убыв" in direction

        def parse_date(tx: Dict[str, Any]) -> datetime:
            d = str(tx.get("date", "1900-01-01"))
            try:
                return datetime.strptime(d, "%d.%m.%Y")
            except ValueError:
                try:
                    return datetime.fromisoformat(d)
                except ValueError:
                    return datetime.min

        data.sort(key=parse_date, reverse=reverse)

    # 3. Только рублевые
    rub_q = input("Выводить только рублевые транзакции? (Да / Нет / Yes / No / Y / N)\n").strip().lower()
    if rub_q in ("да", "yes", "y"):
        data = [
            tx for tx in data
            if str(tx.get("operationAmount", {}).get("currency", {}).get("name", "")).upper() == "RUB"
        ]

    # 4. Поиск по слову
    word_q = input("Отфильтровать список транзакций по определенному слову в описании? (Да / Нет / Yes / No / Y / N)\n").strip().lower()
    if word_q in ("да", "yes", "y"):
        search_word = input("Введите слово для поиска:\n").strip()
        data = process_bank_search(data, search_word)

    # 5. Вывод результата
    print("Распечатываю итоговый список транзакций...")
    if not data:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(data)}\n")
        for tx in data:
            date = tx.get("date", "")
            desc = tx.get("description", "")
            amount = tx.get("operationAmount", {}).get("amount", 0)
            curr = str(tx.get("operationAmount", {}).get("currency", {}).get("name", "RUB"))
            curr_display = "руб." if curr.upper() == "RUB" else curr
            print(f"{date} {desc}")
            print(f"Сумма: {amount} {curr_display}\n")


if __name__ == "__main__":
    main()
