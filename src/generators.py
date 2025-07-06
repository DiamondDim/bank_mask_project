from typing import Iterator, Dict, Any, List


def filter_by_currency(
        transactions: List[Dict[str, Any]],
        currency_code: str
) -> Iterator[Dict[str, Any]]:
    """
    Фильтрует транзакции по коду валюты с улучшенной обработкой ошибок.

    Args:
        transactions: Список транзакций (может содержать None или некорректные данные)
        currency_code: Код валюты (например, "USD")

    Yields:
        Транзакции с указанной валютой
    """
    for transaction in transactions:
        try:
            if transaction is None:
                continue

            op_amount = transaction.get("operationAmount", {})
            curr = op_amount.get("currency", {})
            if curr.get("code") == currency_code:
                yield transaction
        except (AttributeError, TypeError):
            continue


def transaction_descriptions(
        transactions: List[Dict[str, Any]]
) -> Iterator[str]:
    """
    Генератор описаний транзакций с защитой от ошибок.

    Args:
        transactions: Список транзакций (может содержать некорректные данные)

    Yields:
        Описание каждой транзакции или "Нет описания" для некорректных данных
    """
    for transaction in transactions:
        try:
            yield transaction["description"]
        except (KeyError, TypeError):
            yield "Нет описания"


def card_number_generator(
        start: int,
        end: int,
        *,
        step: int = 1,
        card_format: str = "XXXX XXXX XXXX XXXX"  # Переименовано с format на card_format
) -> Iterator[str]:
    """
    Усовершенствованный генератор номеров карт.

    Args:
        start: Начальный номер (≥1)
        end: Конечный номер (≥start)
        step: Шаг генерации (по умолчанию 1)
        card_format: Формат вывода (по умолчанию "XXXX XXXX XXXX XXXX")

    Yields:
        Номера карт в заданном формате

    Raises:
        ValueError: При некорректных параметрах
    """
    if start < 1 or end < start or step < 1:
        raise ValueError("Некорректные параметры генерации")

    for number in range(start, end + 1, step):
        num_str = f"{number:016d}"
        parts = [
            num_str[i * 4:(i + 1) * 4]
            for i in range(len(card_format.split()))  # Использовано card_format вместо format
        ]
        yield " ".join(parts)
