from unittest.mock import mock_open, patch

from src.utils import load_operations


def test_load_operations_success():
    """Успешная загрузка валидного JSON."""
    mock_data = '[{"id": 1, "state": "EXECUTED"}]'

    with patch("builtins.open", mock_open(read_data=mock_data)):
        with patch("pathlib.Path.exists", return_value=True):
            result = load_operations("data/operations.json")

    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0]["id"] == 1


def test_load_operations_file_not_found():
    """Файл не найден → пустой список."""
    with patch("pathlib.Path.exists", return_value=False):
        result = load_operations("nonexistent.json")

    assert result == []


def test_load_operations_invalid_json():
    """Битый JSON → пустой список."""
    with patch("builtins.open", mock_open(read_data="{ invalid json }")):
        with patch("pathlib.Path.exists", return_value=True):
            result = load_operations("data/broken.json")

    assert result == []
