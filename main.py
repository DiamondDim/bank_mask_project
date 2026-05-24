"""
Точка входа в проект bank_mask_project.
Запускает загрузку транзакций, демонстрацию маскировки и конвертацию.
"""
from src.utils import load_operations
from src.masks import get_mask_card_number, get_mask_account
from src.external_api import convert_currency


if __name__ == "__main__":
    # 1. Тест загрузки JSON (логи пишутся в logs/utils.log)
    data = load_operations("data/operations.json")
    load_operations("data/ghost_file.json")  # Сгенерирует WARNING

    # 2. Тест маскировки (логи пишутся в logs/masks.log)
    if data:
        card = data[0].get("description", "40817810400000000000")[:16].isdigit() and data[0].get("description", "")[:16] or "4276550012345678"
        get_mask_card_number(card)
        get_mask_account("40817810400000000000")

    # 3. Тест конвертации (логи пишутся в консоль + logs/utils.log, т.к. external_api использует тот же логгер)
    for tx in data[:3]:
        convert_currency(tx)

