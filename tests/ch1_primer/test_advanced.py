import pytest

from python_dsa.ch1_primer.advanced import num_2_div


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
