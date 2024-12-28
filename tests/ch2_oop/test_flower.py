import pytest

from python_dsa.ch2_oop.flower import Flower


def test_flower_initialization():
    flower = Flower("Rose", 5, 10.99)
    assert flower.get_name() == "Rose"
    assert flower.get_num_petals() == 5
    assert flower.get_price() == 10.99


def test_setters_and_getters():
    flower = Flower("Tulip", 3, 5.50)
    flower.set_name("Daisy")
    assert flower.get_name() == "Daisy"

    flower.set_num_petals(8)
    assert flower.get_num_petals() == 8

    flower.set_price(12.75)
    assert flower.get_price() == 12.75


def test_invalid_name():
    with pytest.raises(ValueError, match="Name must be a string."):
        Flower(123, 5, 10.99)


def test_invalid_num_petals():
    with pytest.raises(
        ValueError, match="Number of petals must be a non-negative integer."
    ):
        Flower("Rose", -1, 10.99)

    with pytest.raises(
        ValueError, match="Number of petals must be a non-negative integer."
    ):
        Flower("Rose", 3.5, 10.99)


def test_invalid_price():
    with pytest.raises(ValueError, match="Price must be a non-negative float."):
        Flower("Rose", 5, -10.99)

    with pytest.raises(ValueError, match="Price must be a non-negative float."):
        Flower("Rose", 5, "expensive")


def test_setters_validation():
    flower = Flower("Lily", 4, 6.75)

    with pytest.raises(ValueError, match="Name must be a string."):
        flower.set_name(456)

    with pytest.raises(
        ValueError, match="Number of petals must be a non-negative integer."
    ):
        flower.set_num_petals(-2)

    with pytest.raises(ValueError, match="Price must be a non-negative float."):
        flower.set_price(-5.99)
