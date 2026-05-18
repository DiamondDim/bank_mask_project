# 🏗️ Архитектура: bank_mask_project
> Статус: Активная разработка | Python 3.13 | Poetry
> Последнее обновление: Май 2026

## 🚀 Быстрый старт
```bash
poetry install --with dev
poetry run pytest --cov=src  # Тесты + покрытие ≥80%
poetry run python main.py    # Запуск CLI
```

## 📁 Структура проекта
```bash
bank_mask_project/
├── data/           # Исходные файлы (JSON, CSV, XLSX)
├── logs/           # Логи (игнорируются Git)
├── src/            # Бизнес-логика
│   ├── utils.py          # Загрузка JSON
│   ├── file_loaders.py   # Загрузчики pandas (CSV/XLSX)
│   ├── masks.py          # Маскировка карт/счетов
│   ├── external_api.py   # Конвертация валют (API)
│   ├── processing.py     # Фильтрация/поиск/Counter
│   ├── widget.py         # Маскировка карты/счета в строке
├── tests/          # Тесты (pytest, mock)
│   ├── test_external_api.py
│   ├── test_file_loaders.py
│   ├── test_masks.py
│   ├── test_processing.py
│   ├── test_utils.py
│   ├── test_widget.py
├── user_settings.json # Настройки пользователя (валюты, акции)
├── main.py         # CLI-интерфейс / Точка входа
├── pyproject.toml  # Зависимости и конфиги
└── ARCH.md         # Файл архитектуры проекта
```

## 🧩 Модули и ответственность
```bash
 Модуль              | Назначение             | Ключевые функции
 --------------------|------------------------|--------------------------------------------------
 utils.py            | Парсинг JSON           | load_operations()
 file_loaders.py     | Парсинг CSV/XLSX       | load_transactions_csv(), load_transactions_excel()
 masks.py            | Безопасность данных    | get_mask_card_number(), get_mask_account()
 external_api.py     | Внешние данные         | convert_currency(), get_rates()
 processing.py       | Аналитика/Поиск        | process_bank_search(), process_bank_operations()
 main.py             | Оркестрация            | main() — CLI-меню, фильтрация, вывод
```

## Инструменты и стандарты
```bash
Менеджер: Poetry (pyproject.toml)
Тесты: pytest + unittest.mock (покрытие ≥80%, моки для API/файлов)
Линтер: flake8 (≤5 warn), isort, mypy (опционально)
Логирование: logging.getLogger(__name__), уровни INFO/ERROR
Конфиги: .env (секреты), user_settings.json (пользовательские параметры)
```

## 🌿 Git-Workflow
```bash
git checkout -b Homework-XX.X
Код → Тесты → flake8 → Коммит
git push → PR в develop
Ссылка на PR → Наставнику
⚠️ В коммиты не попадают: logs/, .env, __pycache__/, .venv/
```

## Как добавлять функционал (Чек-лист)
```bash
Создать функцию в src/ с docstring и типизацией
Добавить логирование успеха/ошибок
Написать тесты (успех + краевые случаи + моки для API/файлов)
Обновить README.md и ARCH.md (при изменении структуры)
Прогнать pytest --cov и flake8
```

## 🆘 Быстрая диагностика
```bash
 Проблема                      | Решение
 ------------------------------|-----------------------------------------------
 ModuleNotFoundError           | poetry install
 Тесты падают на API           | Использовать @patch для requests.get
 NaN в данных из pandas        | Обернуть в str() или fillna()
 flake8 ругается на строки     | Разбить через \ или скобки
 Логи не пишутся               | Проверить os.makedirs("logs", exist_ok=True)
```


