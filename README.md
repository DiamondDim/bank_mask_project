# 🛡️ Маскировщик банковских данных

Простая программа для скрытия номеров карт и счетов.

## **_Как использовать_**

1. [Скачайте программу](https://github.com/DiamondDim/bank_mask_project/archive/main.zip)
2. Откройте файл `input.txt` и впишите свои данные:

### Скрыть номер карты
 

``` python
 from src.masks import get_mask_card_number

 
 card = "1234567890123456"
 print(mask_card(card))  # Напечатает: "**** **** **** 3456"
```
### Отфильтровать транзакции
``` python
 from src.processing import filter_by_state

 
 transactions = [
     {"state": "EXECUTED", "sum": "100"},
     {"state": "CANCELED", "sum": "200"}
 ]
 
 print(get_executed(transactions))  # Покажет только выполненные```
```

## **_Пример_**
```
 Входные данные: 
Карта 1234567812345678, Счет 40817810500001234567

 Выходные данные:
Карта **** **** **** 5678, Счет **4567
```

## Генераторы данных

Модуль `generators` предоставляет инструменты для работы с транзакциями:

### Фильтрация по валюте
```python
from src.generators import filter_by_currency

def process_transactions(transactions):
    """Пример использования фильтрации"""
    usd_transactions = filter_by_currency(transactions, "USD")
    first_usd = next(usd_transactions, None)
    if first_usd:
        print(f"Первая USD-транзакция: {first_usd['id']}")

```

### Получение описаний
```python
from src.generators import transaction_descriptions

def print_descriptions(transactions):
    """Пример вывода описаний"""
    print("Операции:")
    for desc in transaction_descriptions(transactions):
        print(f"- {desc}")

```

### Генерация номеров карт
```python
from src.generators import card_number_generator

def generate_cards_example():
    """Пример генерации номеров карт"""
    print("Сгенерированные номера:")
    for card in card_number_generator(1, 5):
        print(card)

```

#### MIT License. Свободное использование и модификация.

© 2025 DiamondDim. Все права защищены.
