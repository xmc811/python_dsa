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


def make_change(charged, given):
    """
    Write a Python program that can “make change.” Your program should
    take two numbers as input, one that is a monetary amount charged and the
    other that is a monetary amount given. It should then return the number
    of each kind of bill and coin to give back as change for the difference
    between the amount given and the amount charged. The values assigned
    to the bills and coins can be based on the monetary system of any current
    or former government. Try to design your program so that it returns as
    few bills and coins as possible.
    """
    if given < charged:
        raise ValueError(
            "Amount given must be greater than or equal to the amount charged."
        )
    bills = [1, 5, 10, 25, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
    changed = int(round((given - charged) * 100))
    d = {}
    for b in bills[::-1]:
        n, changed = changed // b, changed % b
        if n > 0:
            d[b / 100] = int(n)
    return d


def calculator():
    """
    Write a Python program that can simulate a simple calculator, using the
    console as the exclusive input and output device. That is, each input to the
    calculator, be it a number, like 12.34 or 1034, or an operator, like + or =,
    can be done on a separate line. After each such input, you should output
    to the Python console what would be displayed on your calculator.
    """
    allowed = {"+", "-", "*", "/", ".", "(", ")", "="}
    expr_lst = []
    while True:
        s = input("").strip()
        if s == "=":
            break
        expr_lst.append(s)
    expr = "".join(expr_lst)
    for c in expr:
        if not (c.isdigit() or c in allowed):
            raise ValueError(f"Invalid Input: {c}")
    return eval(expr)


def permutations(chars):
    """
    Write a Python program that outputs all possible strings formed by using
    the characters c , a , t , d , o , and g exactly once.
    """

    if len(chars) == 0:
        return [""]
    if len(chars) == 1:
        return [chars]

    res = []
    ps = permutations(chars[1:])
    for p in ps:
        for i in range(len(p) + 1):
            res.append(p[:i] + chars[0] + p[i:])
    return res
