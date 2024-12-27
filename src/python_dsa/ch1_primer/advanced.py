def num_2_div(x):
    """
    Write a Python program that can take a positive integer greater than 2 as
    input and write out the number of times one must repeatedly divide this
    number by 2 before getting a value less than 2.
    """
    if not isinstance(x, int):
        raise TypeError("x must be an integer.")
    if x <= 2:
        raise ValueError("x must be greater than 2.")
    ct = 0
    while x >= 2:
        x /= 2
        ct += 1
    return ct
