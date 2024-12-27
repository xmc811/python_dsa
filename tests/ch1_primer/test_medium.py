import pytest

from python_dsa.ch1_primer.medium import (
    all_distinct,
    arithmatic_order,
    count_vowels,
    dot_product,
    factors,
    has_odd_product,
    norm,
    random_shuffle,
    remove_punctuation,
)


def test_has_odd_product():
    # Test with an empty list
    assert not has_odd_product([])
    # Test with a list of all even numbers
    assert not has_odd_product([2, 4, 6, 8])
    # Test with a single odd number
    assert not has_odd_product([2, 4, 5, 6])
    # Test with exactly two odd numbers
    assert has_odd_product([2, 4, 5, 7])
    # Test with more than two odd numbers
    assert has_odd_product([3, 5, 7, 8])
    # Test with a mix of even and odd numbers
    assert has_odd_product([1, 2, 4, 6, 9])  # Odd numbers: 1, 9
    # Test with negative odd numbers
    assert has_odd_product([-3, 4, -5, 6])  # Odd numbers: -3, -5
    # Test with no distinct odd numbers forming a pair
    assert not has_odd_product([1])  # Only one odd number


def test_all_distinct():
    # Empty list: all elements are distinct
    assert all_distinct([])
    # List with all unique elements
    assert all_distinct([1, 2, 3, 4])
    # List with duplicate elements
    assert not all_distinct([1, 2, 2, 4])
    # List with all identical elements
    assert not all_distinct([5, 5, 5, 5])
    # Mixed data types
    assert all_distinct([1, "1", (1,)])
    # List with nested structures
    assert not all_distinct([(1, 2), (1, 2), (3, 4)])
    # Large list with unique elements
    assert all_distinct(list(range(1000)))
    # Large list with duplicates
    assert not all_distinct(list(range(999)) + [998])


def test_dot_product():
    # Test with empty lists
    assert dot_product([], []) == 0
    # Test with single-element lists
    assert dot_product([2], [3]) == 6
    # Test with multi-element lists
    assert dot_product([1, 2, 3], [4, 5, 6]) == 32
    # Test with negative numbers
    assert dot_product([-1, -2, -3], [1, 2, 3]) == -14
    # Test with mixed positive and negative numbers
    assert dot_product([-1, 2, -3], [4, -5, 6]) == -32
    # Test with zeros
    assert dot_product([0, 0, 0], [1, 2, 3]) == 0
    # Test with large numbers
    assert dot_product([10**6, 10**6], [10**6, -(10**6)]) == 0
    # Test mismatched lengths (should raise ValueError)
    try:
        dot_product([1, 2], [1])
        assert False  # Mismatched lengths should raise ValueError
    except ValueError as e:
        assert str(e) == "Input arrays must have the same length."


def test_count_vowels():
    # Test empty string
    assert count_vowels("") == 0
    # Test string with no vowels
    assert count_vowels("bcdfg") == 0
    # Test string with only vowels
    assert count_vowels("aeiou") == 5
    # Test string with uppercase vowels
    assert count_vowels("AEIOU") == 5
    # Test mixed-case string with vowels and consonants
    assert count_vowels("AbCdEfGhIjKl") == 3
    # Test string with repeated vowels
    assert count_vowels("aaaaeeeiiiooouuu") == 16
    # Test string with numbers and special characters
    assert count_vowels("123!@#aei") == 3


def test_remove_punctuation():
    # Test with empty string
    assert remove_punctuation("") == ""
    # Test with string without punctuation
    assert remove_punctuation("Hello World") == "Hello World"
    # Test with string containing only punctuation
    assert remove_punctuation("!@#$%^&*()") == ""
    # Test with mixed punctuation and text
    assert remove_punctuation("Let's try, Mike.") == "Lets try Mike"
    # Test with string containing numbers and punctuation
    assert remove_punctuation("Price: $100.50!") == "Price 10050"
    # Test with string containing newlines and tabs
    assert (
        remove_punctuation("Hello,\nWorld!\tHow's it going?")
        == "Hello\nWorld\tHows it going"
    )
    # Test with string containing multiple spaces and punctuation
    assert remove_punctuation("Wow!!!   What a day...") == "Wow   What a day"


def test_arithmatic_order():
    # Test simple addition
    assert arithmatic_order(3, 2, 5)
    # Test simple subtraction
    assert arithmatic_order(5, 2, 3)
    # Test multiplication
    assert arithmatic_order(3, 2, 6)
    # Test division
    assert arithmatic_order(6, 2, 3)
    # Test reverse operations (e.g., a = b + c)
    assert arithmatic_order(5, 2, 3)
    # Test no valid arithmetic relation
    assert not arithmatic_order(3, 2, 7)


def test_norm():
    # Test for p = infinity (max norm)
    assert norm([3, -4, 5], p=float("inf")) == 5
    # Test for Euclidean norm (p=2)
    assert norm([3, 4]) == 5.0  # 3^2 + 4^2 = 9 + 16 = 25, sqrt(25) = 5
    # Test for p-norm with p = 1 (Manhattan norm)
    assert norm([1, 2, 3], p=1) == 6  # 1 + 2 + 3 = 6
    # Test for p-norm with p = 3
    assert norm([1, 2, 3], p=3) == (1**3 + 2**3 + 3**3) ** (1 / 3)
    # Assert ValueError is raised for p = 0
    with pytest.raises(ValueError):
        norm([1, 2, 3], p=0)
    # Test with empty list
    assert norm([], p=2) == 0  # No elements to sum, the norm should be 0
    # Test for p-norm with negative numbers
    assert norm([-3, 4], p=2) == 5.0  # (-3)^2 + 4^2 = 9 + 16 = 25, sqrt(25) = 5
    # Test for large numbers
    assert norm([1000, 2000], p=2) == (1000**2 + 2000**2) ** (1 / 2)
    # Test default case for p = 2
    assert norm([1, 2], p=2) == (1**2 + 2**2) ** (1 / 2)


def test_factors():
    # Test for small number
    assert list(factors(6)) == [1, 2, 3, 6]  # Factors of 6 are 1, 2, 3, 6
    # Test for prime number
    assert list(factors(7)) == [1, 7]  # Factors of 7 are 1, 7
    # Test for larger number
    assert list(factors(24)) == [1, 2, 3, 4, 6, 8, 12, 24]
    # Test for a perfect square
    assert list(factors(289)) == [1, 17, 289]
    # Test for edge case 1 (n = 1, which only has one factor)
    assert list(factors(1)) == [1]  # Factors of 1 is only 1
    # Test for edge case 2 (n = 0, which technically has infinite factors but should be empty)
    assert list(factors(0)) == []


def test_random_shuffle():
    # Test 1: Check if shuffle preserves the list length and contents
    lst = [1, 2, 3, 4, 5]
    shuffled_lst = random_shuffle(lst[:])  # Use a copy to preserve original list
    assert len(shuffled_lst) == len(lst)  # Length should be same
    assert set(shuffled_lst) == set(lst)  # All elements should be the same

    # Test 2: Check if the shuffle actually changes the order
    # This test may fail occasionally, as shuffle can result in the same order
    same_order_count = 0
    for _ in range(1000):  # Run multiple times to ensure the shuffle does something
        shuffled_lst = random_shuffle(lst[:])
        if shuffled_lst == lst:
            same_order_count += 1
    assert same_order_count < 50  # Assert that in most cases, the order is shuffled

    # Test 3: Edge case: empty list
    assert random_shuffle([]) == []

    # Test 4: Edge case: single-element list
    assert random_shuffle([42]) == [42]
