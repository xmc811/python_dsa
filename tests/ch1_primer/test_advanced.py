import pytest

from python_dsa.ch1_primer.advanced import (
    calculator,
    make_change,
    num_2_div,
    permutations,
)


def test_num_2_div():
    # Test 1: Basic cases
    assert num_2_div(3) == 1  # 3 / 2 = 1.5 (1 division)
    assert num_2_div(4) == 2  # 4 / 2 = 2, 2 / 2 = 1 (2 divisions)
    assert num_2_div(16) == 4  # 16 -> 8 -> 4 -> 2 -> 1 (4 divisions)
    assert num_2_div(1024) == 10  # 1024 divided 10 times becomes < 2

    # Test 2: Edge case - ValueError for x <= 2
    with pytest.raises(ValueError, match="x must be greater than 2."):
        num_2_div(2)
    with pytest.raises(ValueError, match="x must be greater than 2."):
        num_2_div(1)

    # Test 3: Large input
    assert num_2_div(10**6) == 19  # Large number with many divisions

    # Test 4: Floating-point inputs are not allowed, ensuring only integers are valid
    with pytest.raises(TypeError):
        num_2_div(4.5)


def test_make_change():
    # Test with exact change
    assert make_change(10.00, 10.00) == {}

    # Test with small change
    assert make_change(10.00, 10.05) == {0.05: 1}

    # Test with multiple denominations
    assert make_change(10.00, 17.88) == {5: 1, 2: 1, 0.5: 1, 0.25: 1, 0.1: 1, 0.01: 3}

    # Test with invalid input (given less than charged)
    with pytest.raises(
        ValueError,
        match="Amount given must be greater than or equal to the amount charged.",
    ):
        make_change(10.00, 5.00)


def test_calculator(monkeypatch):
    inputs = iter(["3", "+", "15", "="])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert calculator() == 18

    inputs = iter(["3", "**", "3", "="])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert calculator() == 27

    inputs = iter(["(", "3", "+", "2", ")", "*", "4", "="])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert calculator() == 20

    inputs = iter(["(", "3.2", "+", "2", ")", "*", "4", "="])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert calculator() == 20.8

    inputs = iter(["(3", "+", "5", "="])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    with pytest.raises(SyntaxError):
        calculator()

    inputs = iter(["10", "/", "0", "="])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    with pytest.raises(ZeroDivisionError):
        calculator()

    inputs = iter(["3", "+", "five", "="])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    with pytest.raises(ValueError):
        calculator()


def test_permutations():
    # Test empty input
    assert permutations("") == [""]

    # Test single character
    assert permutations("a") == ["a"]

    # Test two characters
    assert sorted(permutations("ab")) == sorted(["ab", "ba"])

    # Test all unique characters
    assert len(permutations("catdog")) == 720  # 6! = 720 permutations
    assert "catdog" in permutations("catdog")
    assert "godtac" in permutations("catdog")

    # Test basic input
    assert sorted(permutations("cat")) == sorted(
        ["cat", "cta", "act", "atc", "tca", "tac"]
    )

    # Test duplicates
    assert sorted(permutations("aa")) == sorted(
        ["aa", "aa"]
    )  # Should handle repeated characters correctly
