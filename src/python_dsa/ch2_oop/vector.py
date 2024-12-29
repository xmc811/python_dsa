class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, data):
        """Create a vector, with coordinates or dimensions"""
        if isinstance(data, int):
            self._coords = [0] * data
        elif isinstance(data, (list, tuple)):
            self._coords = data
        else:
            raise TypeError("Unsupported data type.")

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, j):
        """Return jth coordinate of vector."""
        return self._coords[j]

    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):
            raise ValueError("Dimensions must agree")
        return Vector([x + y for x, y in zip(self._coords, other._coords)])

    def __neg__(self):
        """Return the negation of the vector."""
        return Vector([-x for x in self._coords])

    def __sub__(self, other):
        """Return subtraction of two vectors."""
        if len(self) != len(other):
            raise ValueError("Dimensions must agree")
        return self + (-other)

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector([x * other for x in self._coords])
        elif isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError("Dimensions must agree")
            return sum([x * y for x, y in zip(self._coords, other._coords)])

    def __rmul__(self, other):
        return self * other

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other

    def __str__(self):
        """Produce string representation of vector."""
        return "<" + str(self._coords) + ">"
