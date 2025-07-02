import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.fixture
def valid_card_numbers():
    return [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1234567890123456", "1234 56** **** 3456")
    ]

@pytest.fixture
def valid_account_numbers():
    return [
        ("73654108430135874305", "**4305"),
        ("12345678901234567890", "**7890")
    ]

@pytest.fixture
def invalid_inputs():
    return [
        ("123", "Слишком короткий номер"),
        ("12a45", "Содержит буквы"),
        ("123456789012345", "15 цифр")
    ]

def test_mask_card_valid(valid_card_numbers):
    for number, expected in valid_card_numbers:
        assert get_mask_card_number(number) == expected

def test_mask_card_empty():
    assert get_mask_card_number("") == ""

def test_mask_card_invalid(invalid_inputs):
    for number, _ in invalid_inputs[:2]:
        with pytest.raises(ValueError):
            get_mask_card_number(number)

def test_mask_account_valid(valid_account_numbers):
    for number, expected in valid_account_numbers:
        assert get_mask_account(number) == expected

def test_mask_account_empty():
    assert get_mask_account("") == ""

def test_mask_account_invalid(invalid_inputs):
    for number, _ in invalid_inputs[:2]:
        with pytest.raises(ValueError):
            get_mask_account(number)


@pytest.mark.parametrize("card_or_account,expected,is_valid", [
    ("", "", True),
    ("1234", "**1234", True),
    ("123", None, False),
    ("1234567890123456", "1234 56** **** 3456", True),
    ("12a34", None, False)
])
def test_masks_combined(card_or_account, expected, is_valid):
    if not is_valid:
        with pytest.raises(ValueError):
            if len(card_or_account) <= 4:
                get_mask_account(card_or_account)
            else:
                get_mask_card_number(card_or_account)
    else:
        if len(card_or_account) <= 4 and card_or_account:
            assert get_mask_account(card_or_account) == expected
        elif card_or_account:
            assert get_mask_card_number(card_or_account) == expected