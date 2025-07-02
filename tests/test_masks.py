import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.fixture
def sample_card_numbers():
    return [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1234567890123456", "1234 56** **** 3456")
    ]

@pytest.fixture
def sample_account_numbers():
    return [
        ("73654108430135874305", "**4305"),
        ("12345678901234567890", "**7890")
    ]

def test_mask_card(sample_card_numbers):
    for number, expected in sample_card_numbers:
        assert get_mask_card_number(number) == expected

def test_mask_account(sample_account_numbers):
    for number, expected in sample_account_numbers:
        assert get_mask_account(number) == expected