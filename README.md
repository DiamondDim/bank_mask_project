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

## 🛠 Генераторы данных

Модуль `generators` предоставляет инструменты для обработки банковских транзакций:

### 1. Фильтрация транзакций по валюте
``` python
from src.generators import filter_by_currency

transactions = [...]  # Ваши транзакции
usd_transactions = filter_by_currency(transactions, "USD")

# Получить первые 2 USD-транзакции
for _ in range(2):
    print(next(usd_transactions))
```
### Получение описаний
``` python
from src.generators import transaction_descriptions

for desc in transaction_descriptions(transactions):
    print(desc)  # Выводит описания по одной
```

### Генерация номеров карт
``` python
from src.generators import card_number_generator

# Сгенерировать номера с 1 по 5
for card in card_number_generator(1, 5):
    print(card)  # 0000 0000 0000 0001 ... 0000 0000 0000 0005
```

#### MIT License. Свободное использование и модификация.

© 2025 DiamondDim. Все права защищены.
