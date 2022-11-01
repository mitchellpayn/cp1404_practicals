"""
Test file for guitar.py
"""
from guitar import Guitar

name = "Gibson L-5 CES"
year = 1922
cost = 16035.40

guitar = Guitar(name, year, cost)
another_guitar = Guitar("another guitar", 2020, 50)
print(f"{name} get_age() - Expected 100. Got {guitar.get_age()}")
print(f"{name} is_vintage() - Expected True. Got {guitar.is_vintage()}")
print(f"{another_guitar.name} get_age() - Expected 2. Got {another_guitar.get_age()}")
print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")