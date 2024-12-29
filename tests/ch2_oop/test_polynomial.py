import pytest

from python_dsa.ch2_oop.polynomial import Term, num_to_str, parse_term_str


def test_parse_term_str():
    # Valid cases
    assert parse_term_str("3x") == (3.0, "x", 1)
    assert parse_term_str("-3x^2") == (-3.0, "x", 2)
    assert parse_term_str("32x^2") == (32.0, "x", 2)
    assert parse_term_str("3.5*x^3") == (3.5, "x", 3)
    assert parse_term_str("x") == (1.0, "x", 1)
    assert parse_term_str("x^4") == (1.0, "x", 4)
    assert parse_term_str("-x^2") == (-1.0, "x", 2)
    assert parse_term_str("3") == (3.0, "", 1)

    # Additional cases with negative numbers
    assert parse_term_str("-3.5*x^3") == (-3.5, "x", 3)
    assert parse_term_str("3*x^-2") == (3.0, "x", -2)

    # Invalid cases (expecting ValueError)
    with pytest.raises(ValueError):
        parse_term_str("3**2")  # Missing variable

    with pytest.raises(ValueError):
        parse_term_str("3x^")  # Missing exponent

    with pytest.raises(ValueError):
        parse_term_str("x^2^")  # Invalid exponent format

    with pytest.raises(ValueError):
        parse_term_str("abc")  # Invalid term format

    with pytest.raises(ValueError):
        parse_term_str("3x1")  # Invalid, should not match


def test_num_to_str():
    # Valid cases
    assert num_to_str(3) == "3"  # Positive integer, no sign needed
    assert num_to_str(-3) == "-3"  # Negative integer, sign included
    assert num_to_str(1.0) == ""  # 1.0 is converted to "1" (no decimal part)
    assert num_to_str(-1.0) == "-"  # -1.0 is converted to "-1" (no decimal part)
    assert num_to_str(3.5) == "3.5"  # Positive decimal
    assert num_to_str(-3.5) == "-3.5"  # Negative decimal
    assert num_to_str(0) == "0"  # Zero case
    assert num_to_str(-0) == "0"  # Negative zero is treated as zero

    # Edge cases for values close to 1 and -1
    assert num_to_str(1) == ""  # 1 as integer should return "1"
    assert num_to_str(-1) == "-"  # -1 as integer should return "-1"

    # Floating point precision
    assert num_to_str(1.00000001) == "1.00000001"  # A very small decimal part after 1
    assert (
        num_to_str(-1.00000001) == "-1.00000001"
    )  # A very small decimal part after -1

    # Large number cases
    assert num_to_str(1000) == "1000"  # Large positive integer
    assert num_to_str(-1000) == "-1000"  # Large negative integer
    assert num_to_str(1000.5) == "1000.5"  # Large positive decimal
    assert num_to_str(-1000.5) == "-1000.5"  # Large negative decimal


def test_term_init():
    term = Term("3x^2")
    assert term.coefficient == 3
    assert term.variable == "x"
    assert term.exponent == 2

    term = Term([3, "x", 2])
    assert term.coefficient == 3
    assert term.variable == "x"
    assert term.exponent == 2

    term = Term("x")
    assert term.coefficient == 1
    assert term.variable == "x"
    assert term.exponent == 1

    term = Term("-x^-1")
    assert term.coefficient == -1
    assert term.variable == "x"
    assert term.exponent == -1


def test_term_str():
    term = Term("3x^2")
    assert str(term) == "3x^2"

    term = Term("1x^3")
    assert str(term) == "x^3"

    term = Term("-x^0")
    assert str(term) == "-1"

    term = Term("-3x^0")
    assert str(term) == "-3"

    term = Term("3x")
    assert str(term) == "3x"


def test_term_equality():
    term1 = Term((3, "x", 2))
    term2 = Term("3x^2")
    term3 = Term((3, "y", 2))
    term4 = Term((4, "x", 2))
    term5 = Term((3, "x", 3))

    # Positive equality case
    assert term1 == term2
    assert term1 != term3
    assert term1 != term4
    assert term1 != term5


def test_term_addition():
    term1 = Term("3x^2")
    term2 = Term((4, "x", 2))
    term3 = Term((-3, "x", 2))
    term4 = Term((4, "x", 3))
    term5 = Term((5, "", 1))
    term6 = Term("3")
    term7 = Term("0x")

    result = term1 + term2
    assert result.coefficient == 7
    assert result.variable == "x"
    assert result.exponent == 2

    result = term1 + term3
    assert result.coefficient == 0
    assert result.variable == ""
    assert result.exponent == 1

    with pytest.raises(ValueError, match="Cannot be merged."):
        term1 + term4

    result = term5 + term6
    assert result.coefficient == 8
    assert result.variable == ""
    assert result.exponent == 1

    result = term6 + term7
    assert result.coefficient == 3
    assert result.variable == ""
    assert result.exponent == 1


def test_term_negation():
    term1 = Term("3x^2")
    term2 = -term1

    assert term2.coefficient == -3
    assert term2.variable == "x"
    assert term2.exponent == 2


def test_term_subtraction():
    term1 = Term("3x^2")
    term2 = Term((4, "x", 2))
    term3 = Term((-3, "x", 2))
    term4 = Term("0x")

    result = term1 - term2
    assert result.coefficient == -1
    assert result.variable == "x"
    assert result.exponent == 2

    result = term1 - term1
    assert result.coefficient == 0
    assert result.variable == ""
    assert result.exponent == 1

    result = term1 - term3
    assert result.coefficient == 6
    assert result.variable == "x"
    assert result.exponent == 2

    assert term1 + term4 == term1
    assert term4 + term1 == term1
