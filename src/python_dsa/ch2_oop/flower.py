class Flower:
    """
    Write a Python class, Flower, that has three instance variables of type str,
    int, and float, that respectively represent the name of the flower, its number
    of petals, and its price. Your class must include a constructor method
    that initializes each variable to an appropriate value, and your class should
    include methods for setting the value of each type, and retrieving the value
    of each type.
    """

    def __init__(self, name, num_petals, price):
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        if not isinstance(num_petals, int) or num_petals < 0:
            raise ValueError("Number of petals must be a non-negative integer.")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative float.")
        self.name = name
        self.num_petals = num_petals
        self.price = price

    def get_name(self):
        return self.name

    def get_num_petals(self):
        return self.num_petals

    def get_price(self):
        return self.price

    def set_name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        self.name = name

    def set_num_petals(self, num_petals):
        if not isinstance(num_petals, int) or num_petals < 0:
            raise ValueError("Number of petals must be a non-negative integer.")
        self.num_petals = num_petals

    def set_price(self, price):
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative float.")
        self.price = price
