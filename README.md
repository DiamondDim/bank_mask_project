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
```
```
\bank_mask_project_homework_10_1> pytest -v
======================================================================================================= test session starts =======================================================================================================
platform win32 -- Python 3.13.3, pytest-8.4.1, pluggy-1.6.0 -- C:\Users\Dmitriy\AppData\Local\pypoetry\Cache\virtualenvs\project-bank-masks-9EeReD3e-py3.13\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Dmitriy\Desktop\bank_mask_project_homework_10_1
configfile: pyproject.toml
plugins: cov-6.2.1
collected 19 items                                                                                                                                                                                                                 

tests/test_masks.py::test_mask_card_valid PASSED                                                                                                                                                                             [  5%] 
tests/test_masks.py::test_mask_card_empty PASSED                                                                                                                                                                             [ 10%] 
tests/test_masks.py::test_mask_card_invalid PASSED                                                                                                                                                                           [ 15%]
tests/test_masks.py::test_mask_account_valid PASSED                                                                                                                                                                          [ 21%] 
tests/test_masks.py::test_mask_account_empty PASSED                                                                                                                                                                          [ 26%] 
tests/test_masks.py::test_mask_account_invalid PASSED                                                                                                                                                                        [ 31%]
tests/test_masks.py::test_masks_combined[--True] PASSED                                                                                                                                                                      [ 36%] 
tests/test_masks.py::test_masks_combined[1234-**1234-True] PASSED                                                                                                                                                            [ 42%] 
tests/test_masks.py::test_masks_combined[123-None-False] PASSED                                                                                                                                                              [ 47%] 
tests/test_masks.py::test_masks_combined[1234567890123456-1234 56** **** 3456-True] PASSED                                                                                                                                   [ 52%] 
tests/test_masks.py::test_masks_combined[12a34-None-False] PASSED                                                                                                                                                            [ 57%]
tests/test_processing.py::test_filter_by_state_default PASSED                                                                                                                                                                [ 63%] 
tests/test_processing.py::test_filter_by_state_executed PASSED                                                                                                                                                               [ 68%] 
tests/test_processing.py::test_filter_by_state_canceled PASSED                                                                                                                                                               [ 73%] 
tests/test_processing.py::test_sort_by_date_descending PASSED                                                                                                                                                                [ 78%]
tests/test_processing.py::test_sort_by_date_ascending PASSED                                                                                                                                                                 [ 84%] 
tests/test_widget.py::test_mask_account_card[Visa Platinum 7000792289606361-Visa Platinum 7000 79** **** 6361] PASSED                                                                                                        [ 89%] 
tests/test_widget.py::test_mask_account_card[\u0421\u0447\u0435\u0442 73654108430135874305-\u0421\u0447\u0435\u0442 **4305] PASSED                                                                                           [ 94%] 
tests/test_widget.py::test_get_date PASSED                                                                                                                                                                                   [100%]

========================================================================================================= tests coverage ========================================================================================================== 
_________________________________________________________________________________________ coverage: platform win32, python 3.13.3-final-0 _________________________________________________________________________________________ 

Coverage HTML written to dir htmlcov
======================================================================================================= 19 passed in 0.30s ======================================================================================================== 
```



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
