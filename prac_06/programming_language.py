"""
programming language class
"""


class ProgrammingLanguage:
    """programming language class for sorting object information"""


def __init__(self, name="", typing="", reflection="", year=0):
    """"""
    self.name = name
    self.typing = typing
    self.reflection = reflection
    self.year = year


def __str__(self):
    return f"{self.name}, {self.typing} typing, Reflection={self.reflection}, First appeared in {self.year}"


def is_dynamic(self):
    return self.typing == "Dynamic"
