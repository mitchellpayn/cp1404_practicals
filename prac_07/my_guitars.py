"""
Practical 7 More Guitars
"""
from prac_06.guitar import Guitar

in_file = open('guitars.csv', 'r')
guitars = []
for line in in_file:
    parts = line.strip().split(',')
    guitars.append(Guitar(parts[0], parts[1], parts[2]))
guitars.sort()
for guitar in guitars:
    print(guitar)
