"""
Guitar class Prac 6
"""
CURRENT_YEAR = 2022


class Guitar:
    """Guitar class for sorting guitar information"""
    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        return self.get_age() >= 50

    def __lt__(self, other):
        """Less than, used for sorting Guitars - by year released."""
        return self.year < other.year
