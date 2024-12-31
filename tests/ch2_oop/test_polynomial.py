import pytest

from python_dsa.ch2_oop.polynomial import Term, build_expression, parse_expression


@pytest.mark.parametrize(
    "expr, expected_coef, expected_vars",
    [
        ("3.5(x^2)(y^2)(z^2)", 3.5, {"x": 2, "y": 2, "z": 2}),
        ("-3.5(x^2)(y^2)(z^2)", -3.5, {"x": 2, "y": 2, "z": 2}),
        ("(x^2)(y^2)(z^2)", 1, {"x": 2, "y": 2, "z": 2}),
        ("(x)(y^3)(z)", 1, {"x": 1, "y": 3, "z": 1}),
        ("-(x^2)(y)(z^3)", -1, {"x": 2, "y": 1, "z": 3}),
        ("-(x^2)", -1, {"x": 2}),
        ("-2.5(x^3)", -2.5, {"x": 3}),
        ("(y^5)(z)", 1, {"y": 5, "z": 1}),
        ("-(y^4)", -1, {"y": 4}),
        ("(a)(b^2)(c^3)", 1, {"a": 1, "b": 2, "c": 3}),
        ("-4.0(x)", -4.0, {"x": 1}),
        ("(x)", 1, {"x": 1}),
        ("5", 5, {}),
        ("-7.5", -7.5, {}),
        ("1", 1, {}),
        ("-1", -1, {}),
        ("0", 0, {}),
    ],
)
def test_parse_term_str_valid(expr, expected_coef, expected_vars):
    coef, variables = parse_expression(expr)
    assert coef == pytest.approx(expected_coef)
    assert variables == expected_vars


@pytest.mark.parametrize(
    "coef, vars_dict, expected_expr",
    [
        (3.5, {"x": 2, "y": 2, "z": 2}, "3.5(x^2)(y^2)(z^2)"),
        (-3.5, {"x": 2, "y": 2, "z": 2}, "-3.5(x^2)(y^2)(z^2)"),
        (1, {"x": 1, "y": 3, "z": 1}, "(x)(y^3)(z)"),
        (-1, {"x": 2, "y": 1, "z": 3}, "-(x^2)(y)(z^3)"),
        (5, {}, "5"),
        (-7.5, {}, "-7.5"),
        (1, {"x": 1}, "(x)"),
        (-1, {"x": 1}, "-(x)"),
    ],
)
def test_build_expression(coef, vars_dict, expected_expr):
    assert build_expression(coef, vars_dict) == expected_expr


def test_term_equality():
    term1 = Term((3, {"x": 2}))
    term2 = Term("3(x^2)")
    term3 = Term((3, {"y": 2}))

    # Positive equality case
    assert term1 == term2
    assert term1 != term3


def test_term_addition():
    term1 = Term("3(x^2)")
    term2 = Term((-2, {"x": 2}))
    term3 = Term((-3, {"x": 2}))
    term4 = Term((4, {"x": 3}))

    term5 = Term((5, {}))
    term6 = Term("3")
    term7 = Term("0(x)(y^2)")

    result = term1 + term2
    assert result == Term("(x^2)")

    result = term1 + term3
    assert result == Term("0")

    with pytest.raises(ValueError, match="Cannot be merged."):
        term1 + term4

    result = term5 + term6
    assert result == Term("8")

    result = term6 + term7
    assert result == Term("3")

    assert term6 + term7 == term7 + term6

    assert term1 + term7 == term1
    assert term7 + term1 == term1


def test_term_negation():
    term1 = Term("3(x^2)")
    term2 = -term1
    term3 = Term("0(x)")

    assert term2 == Term((-3, {"x": 2}))
    assert term3 == -term3


def test_term_subtraction():
    term1 = Term("3(x^2)")
    term2 = Term((-1, {"x": 2}))

    result = term1 - term2
    assert result == Term((4, {"x": 2}))

    result = term1 - term1
    assert result == Term("0")


@pytest.mark.parametrize(
    "term1, term2, expected_coef, expected_vars",
    [
        # Test cases with various combinations of terms
        ("3.5(x^2)(y^2)", "2(x)(z^2)", 7.0, {"x": 3, "y": 2, "z": 2}),
        ("3.5(x^2)(y^2)", "1(x^2)(z^3)", 3.5, {"x": 4, "y": 2, "z": 3}),
        ("1(x^2)(y^3)", "2(x)(z)", 2, {"x": 3, "y": 3, "z": 1}),
        ("-2(x^3)(y)", "-3(x^2)(z^2)", 6, {"x": 5, "y": 1, "z": 2}),
        ("0(x)", "5(y)", 0, {}),
        ("8(x)", "0(y)", 0, {}),
        ("5", "3(x^2)", 15, {"x": 2}),
    ],
)
def test_term_mul(term1, term2, expected_coef, expected_vars):
    # Create Term objects
    term_obj1 = Term(term1)
    term_obj2 = Term(term2)

    # Multiply the terms
    result = term_obj1 * term_obj2

    # Assert coefficient and variables are correct
    assert result.coefficient == expected_coef
    assert result.variables == expected_vars


@pytest.mark.parametrize(
    "term, var, expected_coef, expected_vars",
    [
        ("3.5(x^2)(y^3)", "x", 7.0, {"x": 1, "y": 3}),
        ("3.5(x^2)(y^3)", "y", 10.5, {"x": 2, "y": 2}),
        ("3.5(x^0)(y^3)", "x", 0, {}),
        ("3.5(x^2)(y^3)", "z", 0, {}),
        ("5(x^1)", "x", 5, {}),
    ],
)
def test_derivative(term, var, expected_coef, expected_vars):
    # Create Term object from string representation
    term_obj = Term(parse_expression(term))

    # Get the derivative
    result = term_obj.derivative(var)

    # Assert coefficient and variables are correct
    assert result.coefficient == expected_coef
    assert result.variables == expected_vars
