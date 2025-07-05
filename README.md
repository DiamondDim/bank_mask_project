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
## Тестирование
Запуск тестов с покрытием:
```
pytest -v

## **_Пример_**
```
 Входные данные: 
Карта 1234567812345678, Счет 40817810500001234567

 Выходные данные:
Карта **** **** **** 5678, Счет **4567
```

#### _Этот проект распространяется под лицензией MIT._
MIT License - можно свободно использовать.

© 2025 DiamondDim. Все права защищены.
