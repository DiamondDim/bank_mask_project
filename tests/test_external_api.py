from unittest.mock import Mock, patch

from src.external_api import convert_currency


def test_convert_rub_no_api_call():
    """Рубли не требуют запроса к API."""
    transaction = {"operationAmount": {"amount": "1000", "currency": {"name": "RUB"}}}
    result = convert_currency(transaction)
    assert result == 1000.0


@patch("src.external_api.requests.get")
def test_convert_usd_with_mock(mock_get):
    """Конвертация USD с мокированным запросом."""
    # Настраиваем фейковый ответ
    mock_response = Mock()
    mock_response.json.return_value = {"rates": {"RUB": 75.5}}
    mock_response.raise_for_status = Mock()
    mock_get.return_value = mock_response

    transaction = {"operationAmount": {"amount": "100", "currency": {"name": "USD"}}}

    result = convert_currency(transaction)

    # Проверяем результат
    assert result == 7550.0  # 100 * 75.5

    # Проверяем, что запрос был сделан правильно
    mock_get.assert_called_once()
