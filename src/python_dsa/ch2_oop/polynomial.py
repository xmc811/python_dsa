import re


def parse_expression(expr):
    """
    Parses an algebraic expression into a coefficient and variables with exponents.

    Args:
        expr (str): The algebraic expression (e.g., "-3(x^2)(y)").

    Returns:
        tuple: A coefficient (float) and a dictionary of variables with exponents.
    """
    # Regex to match the coefficient and the variables with exponents
    pattern = r"^(-?[\d.]+)?|\((\w+)(?:\^(\d+))?\)"
    matches = re.findall(pattern, expr)

    # Initialize coefficient and dictionary for variables
    coefficient = 1
    variables = {}

    for match in matches:
        if match[0]:
            coefficient = float(match[0]) if match[0] else 1
        elif match[1]:
            variable = match[1]
            exponent = int(match[2]) if match[2] else 1
            variables[variable] = exponent

    # Special case: If the expression starts with "-", treat it as -1
    if expr.strip().startswith("-") and coefficient == 1:
        coefficient = -1

    if not matches or not any(match[1] or match[0] for match in matches):
        raise ValueError(f"Invalid expression: {expr}")

    return coefficient, variables


def build_expression(coefficient, variables):
    """
    Build an algebraic expression from a coefficient and variables with exponents.

    Args:
        coefficient (float): The coefficient of the expression.
        variables (dict): A dictionary where keys are variable names and values are their exponents.

    Returns:
        str: The reconstructed algebraic expression.
    """
    # Convert the coefficient to a string
    if coefficient == int(coefficient):
        coefficient = int(coefficient)

    coef_str = f"{coefficient}" if coefficient != 1 or not variables else ""
    if coefficient == -1 and variables:
        coef_str = "-"

    # Build the variables part
    variables_str = "".join(
        f"({var}^{exp})" if exp > 1 else f"({var})"
        for var, exp in sorted(variables.items())
    )

    return f"{coef_str}{variables_str}"


class Term:
    """
    Represents a single term in a polynomial, consisting of a coefficient and variables with exponents.
    """

    def __init__(self, expr):
        if isinstance(expr, str):
            self.coefficient, self.variables = parse_expression(expr)
        elif isinstance(expr, (list, tuple)):
            self.coefficient = expr[0]
            self.variables = expr[1]
        else:
            raise ValueError(f"Invalid input: {expr}")
        self.remove_zero_exponent()
        if self.is_zero():
            self.set_zero()

    def set_zero(self):
        self.coefficient = 0
        self.variables = {}

    def remove_zero_exponent(self):
        self.variables = {k: v for k, v in self.variables.items() if v != 0}

    def is_zero(self):
        return self.coefficient == 0

    def __str__(self):
        return build_expression(self.coefficient, self.variables)

    def __eq__(self, other):
        return (
            self.coefficient == other.coefficient and self.variables == other.variables
        )

    def __ne__(self, other):
        return not self == other

    def is_similar_to(self, other):
        return self.variables == other.variables

    def __add__(self, other):
        if other.is_zero():
            return self
        if self.is_zero():
            return other
        if self.is_similar_to(other):
            return Term((self.coefficient + other.coefficient, self.variables))
        else:
            raise ValueError("Cannot be combined.")

    def __radd__(self, other):
        return self + other

    def __neg__(self):
        return Term((-self.coefficient, self.variables))

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        coef = self.coefficient * other.coefficient
        merged = self.variables.copy()
        for key, value in other.variables.items():
            merged[key] = merged.get(key, 0) + value
        return Term((coef, merged))

    def __rmul__(self, other):
        return self * other

    def derivative(self, var):
        if var not in self.variables:
            return Term((0, {}))

        coef = self.coefficient * self.variables[var]
        d = self.variables.copy()
        d[var] -= 1

        return Term((coef, d))


class Polynomial:
    """
    Represents a polynomial as a collection of terms.
    """

    def __init__(self, lst):
        self.terms = lst
        self.remove_zero_terms()

    def remove_zero_terms(self):
        self.terms = [term for term in self.terms if not term.is_zero()]

    def __str__(self):
        s = [str(t) for t in self.terms]
        return ", ".join(s)

    def __add__(self, other):
        result = self.terms.copy()
        for u in other.terms:
            for i, t in enumerate(result):
                if t.is_similar_to(u):
                    result[i] = t + u
                    break
            else:
                result.append(u)
        return Polynomial(result)

    def __radd__(self, other):
        return self + other

    def __neg__(self):
        return Polynomial([-t for t in self.terms])

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        result = Polynomial([Term("0")])
        for t in self.terms:
            for u in other.terms:
                result += Polynomial([t * u])
        return result

    def __rmul__(self, other):
        return self * other


if __name__ == "__main__":
    # Term examples
    t1 = Term("3(x^2)(y)")
    t2 = Term("-4(x^2)(y)")
    t3 = Term("(z)")
    t4 = Term("5")

    # Addition of similar terms
    print("t1 + t2:", t1 + t2)

    # Multiplication of terms
    print("t1 * t3:", t1 * t3)

    # Taking derivatives
    print("Derivative of t1 with respect to 'x':", t1.derivative("x"))
    print("Derivative of t1 with respect to 'y':", t1.derivative("y"))
    print("Derivative of t3 with respect to 'z':", t3.derivative("z"))
    print("Derivative of t4 with respect to 'x':", t4.derivative("x"))

    # Polynomial examples
    p1 = Polynomial([Term("3(x)"), Term("4(y)")])
    p2 = Polynomial([Term("-3(x)"), Term("5(z)")])

    # Polynomial addition
    print("p1 + p2:", p1 + p2)

    # Polynomial subtraction
    print("p1 - p2:", p1 - p2)

    # Polynomial multiplication
    p3 = Polynomial([Term("(x)"), Term("(y)")])
    print("p1 * p3:", p1 * p3)

    # Higher-order derivatives
    t5 = Term("6(x^3)(y^2)")
    print(
        "Second derivative of t5 with respect to 'x':",
        t5.derivative("x").derivative("x"),
    )
    print("Mixed derivative of t5 (d^2/dxdy):", t5.derivative("x").derivative("y"))
