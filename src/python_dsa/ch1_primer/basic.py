import random


def is_multiple(n: int, m: int) -> bool:
    """
    Write a short Python function, is multiple(n, m), that takes two integer
    values and returns True if n is a multiple of m, that is, n = mi for some
    integer i, and False otherwise.
    """
    return n % m == 0


def is_even(k: int) -> bool:
    """
    Write a short Python function, is even(k), that takes an integer value and
    returns True if k is even, and False otherwise. However, your function
    cannot use the multiplication, modulo, or division operators.
    """
    even_list = ["0", "2", "4", "6", "8"]
    return str(k)[-1] in even_list


def minmax(data):
    """
    Write a short Python function, minmax(data), that takes a sequence of
    one or more numbers, and returns the smallest and largest numbers, in the
    form of a tuple of length two. Do not use the built-in functions min or
    max in implementing your solution.
    """
    if not data:
        raise ValueError("Data cannot be empty.")

    x_min, x_max = data[0], data[0]
    for x in data[1:]:
        if x < x_min:
            x_min = x
            next
        if x > x_max:
            x_max = x
    return x_min, x_max


def sum_squares(n):
    """
    Write a short Python function that takes a positive integer n and returns
    the sum of the squares of all the positive integers smaller than n.
    """
    if n < 0:
        raise ValueError("n should be positive.")

    return sum([x**2 for x in range(1, n)])


def sum_odd_squares(n):
    """
    Write a short Python function that takes a positive integer n and returns
    the sum of the squares of all the odd positive integers smaller than n.
    """
    if n < 0:
        raise ValueError("n should be positive.")
    return sum([x**2 for x in range(1, n) if not is_even(x)])


def random_choice(lst):
    """
    Python’s random module includes a function choice(data) that returns a
    random element from a non-empty sequence. The random module includes
    a more basic function randrange, with parameterization similar to
    the built-in range function, that return a random choice from the given
    range. Using only the randrange function, implement your own version
    of the choice function.
    """
    if not lst:  # Check if the list is empty
        raise ValueError("Cannot choose from an empty list")
    return lst[random.randrange(len(lst))]
