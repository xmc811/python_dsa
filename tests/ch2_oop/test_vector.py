import pytest

from python_dsa.ch2_oop.vector import Vector  # Replace with the actual file name


def test_initialization_with_zeros():
    v = Vector(3)
    assert len(v) == 3
    assert v[0] == 0 and v[1] == 0 and v[2] == 0


def test_initialization_with_coords():
    v = Vector([1, 2, 3])
    assert len(v) == 3
    assert v[0] == 1 and v[1] == 2 and v[2] == 3


def test_initialization_with_invalid_type():
    with pytest.raises(TypeError, match="Unsupported data type."):
        Vector("vector")


def test_get_and_set_item():
    v = Vector(3)
    v[1] = 5
    assert v[1] == 5


def test_add_vectors():
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    v3 = v1 + v2
    assert v3 == Vector([5, 7, 9])


def test_add_vectors_dimension_mismatch():
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5])
    with pytest.raises(ValueError, match="Dimensions must agree"):
        v1 + v2


def test_equality():
    v1 = Vector([1, 2, 3])
    v2 = Vector([1, 2, 3])
    v3 = Vector([4, 5, 6])
    assert v1 == v2
    assert v1 != v3


def test_string_representation():
    v = Vector([1, 2, 3])
    assert str(v) == "<[1, 2, 3]>"


def test_zero_dimension_vector():
    v = Vector(0)
    assert len(v) == 0
    assert str(v) == "<[]>"


def test_negation():
    v = Vector([1, -2, 3])
    neg_v = -v
    assert neg_v == Vector([-1, 2, -3])


def test_negation_of_zero_vector():
    v = Vector(3)
    neg_v = -v
    assert neg_v == Vector([0, 0, 0])


def test_subtraction():
    v1 = Vector([5, 7, 9])
    v2 = Vector([1, 2, 3])
    v3 = v1 - v2
    assert v3 == Vector([4, 5, 6])


def test_subtraction_dimension_mismatch():
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5])
    with pytest.raises(ValueError, match="Dimensions must agree"):
        v1 - v2


def test_vector_scalar_multiplication():
    v = Vector([1, 2, 3])
    result = v * 2
    assert result == Vector([2, 4, 6])


def test_scalar_vector_multiplication():
    v = Vector([1, 2, 3])
    result = 2 * v
    assert result == Vector([2, 4, 6])


def test_vector_vector_dot_product():
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    result = v1 * v2
    assert result == 32


def test_vector_vector_dot_product_dimension_mismatch():
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5])
    with pytest.raises(ValueError, match="Dimensions must agree"):
        v1 * v2
