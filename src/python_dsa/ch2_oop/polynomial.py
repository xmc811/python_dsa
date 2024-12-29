import re


def parse_term_str(s):
    pattern = r"(-?)(\d+(?:\.\d+)?)?\*?([a-zA-Z]?)(?:(?:\^)(-?\d+))?$"
    match = re.match(pattern, s)
    if match:
        sign = -1 if match.group(1) else 1
        coefficient = sign * (float(match.group(2)) if match.group(2) else 1)
        variable = match.group(3)
        exponent = float(match.group(4)) if match.group(4) else 1
        if coefficient == 0:
            return 0, "", 1
        return coefficient, variable, exponent
    else:
        raise ValueError(f"Invalid term format: {s}")


def num_to_str(num):
    sign = "" if num >= 0 else "-"
    if abs(num) == 1.0:
        coef = ""
    elif int(num) == num:
        coef = str(int(abs(num)))
    else:
        coef = str(abs(num))
    return f"{sign}{coef}"


class Term:
    def __init__(self, expr):
        if isinstance(expr, str):
            self.coefficient, self.variable, self.exponent = parse_term_str(expr)
        elif isinstance(expr, (list, tuple)):
            self.coefficient, self.variable, self.exponent = expr
        else:
            raise ValueError(f"Invalid input: {expr}")

        if self.is_zero():
            self.set_zero()

    def set_zero(self):
        self.coefficient = 0
        self.variable = ""
        self.exponent = 1

    def is_zero(self):
        return self.coefficient == 0

    def __str__(self):
        coef = num_to_str(self.coefficient)
        expn = num_to_str(self.exponent)
        if coef == "0":
            return ""
        if self.exponent == 0:
            if coef == "-":
                return "-1"
            else:
                return f"{coef}"
        if expn == "":
            return f"{coef}{self.variable}"
        return f"{coef}{self.variable}^{expn}"

    def __eq__(self, other):
        return (
            self.coefficient == other.coefficient
            and self.variable == other.variable
            and self.exponent == other.exponent
        )

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        if other.is_zero():
            return self
        if self.is_zero():
            return other
        if self.variable == other.variable and self.exponent == other.exponent:
            return Term(
                (self.coefficient + other.coefficient, self.variable, self.exponent)
            )
        else:
            raise ValueError("Cannot be merged.")

    def __radd__(self, other):
        return self + other

    def __neg__(self):
        return Term((-self.coefficient, self.variable, self.exponent))

    def __sub__(self, other):
        return self + (-other)
