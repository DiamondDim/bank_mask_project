Проект для обработки банковских данных с функциями маскировки, генерации и логирования операций.

## 🛠 Функциональность

### Основные модули

| Модуль | Описание |
|--------|----------|
| `src/decorators.py` | Декоратор для логирования операций |
| `src/generators.py` | Генерация данных и фильтрация транзакций |
| `src/masks.py` | Маскировка банковских карт и счетов |
| `src/processing.py` | Обработка и сортировка транзакций |
| `src/widget.py` | Вспомогательные функции форматирования |

## 📌 Декораторы логирования

### Использование декоратора `@log`

```python
from src.decorators import log

# Логирование в консоль
@log()
def example_func(param: int) -> int:
    return param * 2

# Логирование в файл
@log(filename="Logs/bank_operations.log")
def process_payment(amount: float) -> bool:
    """Обработка платежа"""
    return True
```
# Логируемые данные:

* Дата и время вызова
* Имя функции и аргументы
* Возвращаемое значение
* Ошибки (если возникают)
* Время выполнения

# 📂 Система логирования и отчетов

### Директории для хранения данных


| Директория | Содержание |
|--------|----------|
| `Logs/` | Файлы логов bank_operations.log |
| `HTML_Tests/` | HTML-отчеты о покрытии кода |
| `Test_results/` | Результаты тестов в JUnit-формате |

### Пример структуры логов:
```
text
2023-11-20 14:30:45 - Вызов функции process_payment с аргументами: (100.0,)
2023-11-20 14:30:45 - Функция process_payment выполнена. Результат: True. Время: 0:00:00.002
```

# 🧪 Тестирование

### Запуск тестов через CMD
```
# Стандартный запуск
pytest -v

# С генерацией отчетов
pytest -v --cov=src --cov-report=html:HTML_Tests --junitxml=Test_results/results.xml --log-file=Logs/tests.log
```

# Тесты для декораторов (test_decorators.py)
``` python
def test_log_to_console(capsys):
    @log()
    def add(a, b):
        return a + b
    
    add(2, 3)
    captured = capsys.readouterr()
    assert "Вызов функции add" in captured.out

def test_log_to_file(tmp_path):
    log_file = tmp_path / "test.log"
    
    @log(filename=str(log_file))
    def test_func():
        pass
    
    test_func()
    assert "Вызов функции test_func" in log_file.read_text()
```

# 🚀 Установка

* Клонируйте репозиторий:
```
git clone https://github.com/DiamondDim/bank_mask_project.git
```
* Установите зависимости:
```
poetry install
```

* Активируйте окружение:
```
poetry shell
```

# 📂 Структура проекта
```
.
├── src/
│   ├── decorators.py      # Декораторы логирования
│   ├── generators.py      # Генераторы данных
│   ├── masks.py           # Маскировка данных
│   ├── processing.py      # Обработка транзакций
│   └── widget.py          # Вспомогательные функции
├── tests/
│   ├── test_decorators.py # Тесты декораторов
│   ├── test_generators.py
│   ├── test_masks.py
│   ├── test_processing.py
│   └── test_widget.py
├── Logs/                  # Логи приложения
├── HTML_Tests/            # Отчеты о покрытии
├── Test_results/          # Результаты тестов
├── .flake8                
├── .gitignore             # Игнорируемы файлы и папки
├── main.py                # Демонстрация работы функций проекта
├── poetry.lock            
├── pyproject.toml         # Конфигурация проекта
├── pytest.ini             
└── README.md              # Описание проекта       
```
# 📝 Примеры использования

### Маскировка данных
```python
from src.masks import mask_card_number, mask_account_number
from src.widget import mask_account_card

# Маскировка номера карты
mask_card_number("7000792289606361")  # "7000 79** **** 6361"

# Маскировка номера счета
mask_account_number("73654108430135874305")  # "**4305"

# Универсальная маскировка
mask_account_card("Visa Platinum 7000792289606361")  # "Visa Platinum 7000 79** **** 6361"
mask_account_card("Счет 73654108430135874305")  # "Счет **4305"
```
### Форматирование данных
```python
from src.widget import format_date

# Форматирование даты
format_date("2018-06-30T02:08:58.425572")  # "30.06.2018"
```
### Генераторы
```python
from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions
)

# Генерация номеров карт
list(card_number_generator(1, 3))  # ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]

# Фильтрация по валюте
transactions = [{"operationAmount": {"currency": {"code": "USD"}}}]
list(filter_by_currency(transactions, "USD"))  # [транзакции в USD]

# Получение описаний
list(transaction_descriptions([{"description": "Payment"}]))  # ["Payment"]
```
### Обработка транзакций
```python
from src.processing import filter_by_state, sort_by_date

transactions = [
    {"state": "EXECUTED", "date": "2023-01-01"},
    {"state": "CANCELED", "date": "2023-01-02"}
]

# Фильтрация по статусу
filter_by_state(transactions, "EXECUTED")  # [транзакции со статусом EXECUTED]

# Сортировка по дате
sort_by_date(transactions)  # отсортированные транзакции
```
### Логирование
```python
from src.decorators import log

@log()
def example_func(param):
    return param * 2

@log(filename="operations.log")
def process_transaction(amount):
    return f"Processed {amount}"
```

# 📜 Лицензия

#### MIT License. Свободное использование и модификация.

### `© 2025 DiamondDim. Все права защищены.`
