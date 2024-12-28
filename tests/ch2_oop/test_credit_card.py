import pytest

from python_dsa.ch2_oop.credit_card import CreditCard


@pytest.fixture
def card():
    return CreditCard("John Doe", "Big Bank", "1234 5678 9012 3456", 1000)


@pytest.fixture
def card_non_zero():
    return CreditCard("John Doe", "Big Bank", "1234 5678 9012 3456", 1000, 500)


def test_initial_balance(card):
    assert card.get_balance() == 0


def test_charge_within_limit(card):
    assert card.charge(500) is True
    assert card.get_balance() == 500
    assert card.charge(100) is True
    assert card.get_balance() == 600


def test_charge_exceeding_limit(card):
    assert card.charge(1001) is False
    assert card.get_balance() == 0


def test_charge_invalid_type(card):
    with pytest.raises(TypeError):
        card.charge("not a number")


def test_make_payment(card):
    card.charge(500)
    card.make_payment(200)
    assert card.get_balance() == 300


def test_make_payment_invalid_type(card):
    with pytest.raises(TypeError):
        card.make_payment("not a number")


def test_make_payment_negative(card):
    with pytest.raises(ValueError):
        card.make_payment(-50)


def test_payment_zero(card):
    card.charge(500)
    card.make_payment(0)
    assert card.get_balance() == 500


def test_charge_zero(card):
    assert card.charge(0) is True
    assert card.get_balance() == 0


def test_balance_exceeds_limit_due_to_float(card):
    card.charge(999.99)
    assert card.charge(0.02) is False
    assert card.get_balance() == 999.99


def test_non_zero_initial_balance(card_non_zero):
    assert card_non_zero.get_balance() == 500
