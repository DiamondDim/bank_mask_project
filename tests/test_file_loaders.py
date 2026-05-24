"""Тесты для модуля file_loaders."""
import pytest  # noqa: F401
from unittest.mock import patch, MagicMock
from src.file_loaders import load_transactions_csv, load_transactions_excel


@patch("src.file_loaders.pd.read_csv")
def test_csv_success(mock_read):
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [{"id": 1}]
    mock_read.return_value = mock_df
    assert load_transactions_csv("test.csv") == [{"id": 1}]


@patch("src.file_loaders.pd.read_csv")
def test_csv_error(mock_read):
    mock_read.side_effect = Exception("fail")
    assert load_transactions_csv("bad.csv") == []


@patch("src.file_loaders.pd.read_excel")
def test_excel_success(mock_read):
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [{"id": 2}]
    mock_read.return_value = mock_df
    assert load_transactions_excel("test.xlsx") == [{"id": 2}]


@patch("src.file_loaders.pd.read_excel")
def test_excel_error(mock_read):
    mock_read.side_effect = Exception("fail")
    assert load_transactions_excel("bad.xlsx") == []
