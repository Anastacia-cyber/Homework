from src.widget import mask_account_card, get_data
import pytest


@pytest.mark.parametrize("string, expected_result", [
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("Счет 12345678901234567890", "Счет **7890"),
])
def test_mask_account_card(string, expected_result):
    assert mask_account_card(string) == expected_result


def test_get_data(data):
    assert get_data(data) == "11.07.2018"
