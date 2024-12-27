import random
import string

from .basic import is_even


def has_odd_product(lst):
    """
    Write a short Python function that takes a sequence of integer values and
    determines if there is a distinct pair of numbers in the sequence whose
    product is odd.
    """
    if not lst:
        return False

    lst = set(lst)
    ct = 0
    for x in lst:
        if not is_even(x):
            ct += 1
        if ct >= 2:
            return True
    return False


def all_distinct(lst):
    """
    Write a Python function that takes a sequence of numbers and determines
    if all the numbers are different from each other (that is, they are distinct).
    """
    return len(lst) == len(set(lst))


def random_shuffle(data):
    """
    Python’s random module includes a function shuffle(data) that accepts a
    list of elements and randomly reorders the elements so that each possible
    order occurs with equal probability. The random module includes a
    more basic function randint(a, b) that returns a uniformly random integer
    from a to b (including both endpoints). Using only the randint function,
    implement your own version of the shuffle function.
    """
    n = len(data)
    for i in range(n):
        # Random index from i to n-1
        idx = random.randint(i, n - 1)
        # Swap elements at i and idx
        data[i], data[idx] = data[idx], data[i]
    return data


def dot_product(a, b):
    """
    Write a short Python program that takes two arrays a and b of length n
    storing int values, and returns the dot product of a and b. That is, it returns
    an array c of length n such that c[i] = a[i] · b[i], for i = 0, . . . ,n−1.
    """
    if len(a) != len(b):
        raise ValueError("Input arrays must have the same length.")
    return sum([x1 * x2 for x1, x2 in zip(a, b)])


def count_vowels(s):
    """
    Write a short Python function that counts the number of vowels in a given
    character string.
    """
    vowels = {"a", "e", "i", "o", "u"}
    return sum([c.lower() in vowels for c in s])


def remove_punctuation(s):
    """
    Write a short Python function that takes a string s, representing a sentence,
    and returns a copy of the string with all punctuation removed. For example,
    if given the string "Let s try, Mike.", this function would return
    "Lets try Mike".
    """
    return "".join(c for c in s if c not in string.punctuation)


def arithmatic_order(a, b, c):
    """
    Write a short program that takes as input three integers, a, b, and c, from
    the console and determines if they can be used in a correct arithmetic
    formula (in the given order), like “a+b = c,” “a = b−c,” or “a ∗ b = c.”
    """
    if (a + b == c) or (a - b == c) or (a * b == c) or ((a / b == c) and (b != 0)):
        return True
    elif (a == b + c) or (a == b - c) or (a == b * c) or ((a == b / c) and (c != 0)):
        return True
    else:
        return False


def factors(n):
    """
    In Section 1.8, we provided three different implementations of a generator
    that computes factors of a given integer. The third of those implementations,
    from page 41, was the most efficient, but we noted that it did not
    yield the factors in increasing order. Modify the generator so that it reports
    factors in increasing order, while maintaining its general performance advantages.
    """
    k = 1
    k_lst = []
    while k * k < n:
        if n % k == 0:
            yield k
            k_lst.append(k)
        k += 1
    if k * k == n:
        yield k
    for k in k_lst[::-1]:
        yield n // k


def norm(v, p=2):
    """
    For the special case of p = 2, this results in the traditional Euclidean
    norm, which represents the length of the vector. Give an implementation
    of a function named norm such that norm(v, p) returns the p-norm
    value of v and norm(v) returns the Euclidean norm of v. You may assume
    that v is a list of numbers.
    """
    if p == 0:
        raise ValueError("p = 0 is not a valid norm")
    if p == float("inf"):
        return max(abs(x) for x in v)
    return sum([x**p for x in v]) ** (1 / p)
