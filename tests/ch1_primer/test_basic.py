import pytest

from python_dsa.ch1_primer.basic import (
    is_even,
    is_multiple,
    minmax,
    random_choice,
    sum_odd_squares,
    sum_squares,
)


def test_is_multiple():
    # Test positive multiples
    assert is_multiple(10, 2)
    assert is_multiple(15, 5)

    # Test non-multiples
    assert not is_multiple(10, 3)
    assert not is_multiple(15, 4)

    # Test edge cases
    assert is_multiple(0, 1)  # Zero is a multiple of any number (except zero itself)
    assert is_multiple(0, 10)
    with pytest.raises(ZeroDivisionError):  # m = 0 should raise an exception
        is_multiple(10, 0)

    # Test negative multiples
    assert is_multiple(-10, 2)
    assert is_multiple(-15, -5)
    assert is_multiple(15, -5)
    assert not is_multiple(-10, 3)


def test_is_even():
    # Test even numbers
    assert is_even(2)
    assert is_even(0)
    assert is_even(-4)

    # Test odd numbers
    assert not is_even(1)
    assert not is_even(-3)
    assert not is_even(9)

    # Test edge cases
    assert is_even(1234567890)  # Large even number
    assert not is_even(-123456789)  # Large odd negative number


def test_minmax():
    # Test case 1: Typical case with positive numbers
    assert minmax([1, 3, 5, 2, 4]) == (1, 5)
    # Test case 2: Negative numbers included
    assert minmax([-1, -3, -5, -2, -4]) == (-5, -1)
    # Test case 3: Single element in the list (edge case)
    assert minmax([10]) == (10, 10)
    # Test case 4: Mixed positive and negative numbers
    assert minmax([-1, 0, 1]) == (-1, 1)
    # Test case 5: All elements are the same
    assert minmax([7, 7, 7, 7]) == (7, 7)
    # Test case 6: Empty list should raise an error (edge case)
    with pytest.raises(ValueError):
        minmax([])


def test_sum_squares():
    # Test case 1: Sum of squares of numbers less than 5
    assert sum_squares(5) == 30  # 1^2 + 2^2 + 3^2 + 4^2 = 30
    # Test case 2: Sum of squares of numbers less than 1 (should be 0)
    assert sum_squares(1) == 0  # No numbers smaller than 1
    # Test case 3: Sum of squares of numbers less than 0
    assert sum_squares(0) == 0
    # Test case 4: Sum of squares of larger number (testing performance)
    assert sum_squares(10) == 285  # 1^2 + 2^2 + ... + 9^2 = 285
    # Test case 5: Edge case for sum of squares of numbers less than 0
    with pytest.raises(ValueError):
        sum_squares(-5)
    # The function doesn't explicitly handle negative input; a negative input might raise an error


def test_sum_odd_squares():
    # Test case 1: Sum of squares of odd numbers less than 10
    assert sum_odd_squares(10) == 165
    # Test case 2: Edge case when n is 1 (no odd numbers smaller than 1)
    assert sum_odd_squares(1) == 0  # No odd numbers smaller than 1
    # Test case 3: Sum of squares of odd numbers less than 0
    assert sum_odd_squares(0) == 0
    # Test case 4: Sum of squares of odd numbers less than 4
    assert sum_odd_squares(4) == 10  # 1^2 + 3^2 = 1 + 9 = 10
    # Test case 5: Edge case for negative input
    with pytest.raises(ValueError):
        sum_odd_squares(-5)  # Should raise ValueError


def test_random_choice():
    # Test case 1: Typical case with a small list
    lst = [1, 2, 3]
    result = random_choice(lst)
    assert result in lst  # Ensure the result is an element in the list
    # Test case 2: Typical case with a string list
    lst = ["a", "b", "c"]
    result = random_choice(lst)
    assert result in lst  # Ensure the result is an element in the list
    # Test case 3: Test with a larger list
    lst = list(range(100))  # A list of numbers from 0 to 99
    result = random_choice(lst)
    assert result in lst  # Ensure the result is an element in the list
    # Test case 4: Edge case with a single-element list
    lst = [42]
    assert random_choice(lst) == 42  # Should return 42 since it's the only element
    # Test case 5: Edge case with an empty list (should raise an error)
    with pytest.raises(ValueError):
        random_choice([])  # Should raise ValueError because the list is empty
    # Test case 6: Test randomness by calling multiple times and checking
    lst = [1, 2, 3, 4, 5]
    results = [random_choice(lst) for _ in range(1000)]
    # Ensure that all elements are selected at least once (in practice, not always true, but it should happen with high probability)
    assert all(x in results for x in lst)
