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
##  Логирование
- Модуль `src/utils.py`: логгер с FileHandler → `logs/utils.log`
- Модуль `src/masks.py`: логгер с FileHandler → `logs/masks.log`
- Формат: `%(asctime)s | %(name)s | %(levelname)s | %(message)s`
- Уровень: DEBUG
- Перезапись при запуске: `mode="w"`

## 🧪 Как проверить
1. Запустите: `poetry run python main.py`
2. Проверьте файлы:
   - `logs/utils.log` — загрузка операций
   - `logs/masks.log` — маскировка карт/счетов

## 📄 CSV и Excel
Проект поддерживает загрузку из `.csv` и `.xlsx`:
```python
from src.file_loaders import load_transactions_csv, load_transactions_excel
data = load_transactions_csv("data/transactions.csv")
```

## 📦 Дополнительно
- .gitignore настроен (логи не в репозитории)
- Все функции типизированы
- Линтер flake8: ≤5 предупреждений

#### _Этот проект распространяется под лицензией MIT._
MIT License - можно свободно использовать.

© 2025 DiamondDim. Все права защищены.
