# 🛡️ Маскировщик банковских данных

Программа для скрытия номеров карт и счетов.

## Установка
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/DiamondDim/bank_mask_project.git
   ```
2. Установите зависимости и активация окружения:
   ```bash
   poetry install
   
   poetry shell
   ```

## Использование
### Маскировка карты
```python
from src.masks import get_mask_card_number

card = "1234567890123456"
print(get_mask_card_number(card))  # Выведет: "1234 56** **** 3456"
```

### Фильтрация транзакций
```python
from src.processing import filter_by_state

transactions = [
    {"state": "EXECUTED", "sum": "100"},
    {"state": "CANCELED", "sum": "200"}
]
print(filter_by_state(transactions, "EXECUTED"))  # Только выполненные
```

## Тестирование
```bash
pytest -v  # Все тесты
pytest --cov=src --cov-report=html  # С отчетом покрытия
```
Отчет: `htmlcov/index.html`

## Пример
**Входные данные**:  
Карта `1234567812345678`, Счет `40817810500001234567`  

**Выходные данные**:  
Карта `1234 56** **** 5678`, Счет `**4567`  

## Лицензия
MIT License. Свободное использование и модификация.

© 2025 DiamondDim. Все права защищены.