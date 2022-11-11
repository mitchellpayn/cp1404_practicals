"""
Practical 7 More Guitars
"""
from prac_06.guitar import Guitar


def main():
    guitars = read_guitar_file()
    get_guitar(guitars)
    guitars.sort()
    for guitar in guitars:
        print(guitar)

    with open("guitars.csv", "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name}, {guitar.year}, {guitar.cost}", file=out_file)


def get_guitar(guitars):
    name = input("Name:")
    while name != "":
        year = int(input("Year:"))
        cost = float(input("Cost:"))
        guitar_to_add = [name, year, cost]
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost} added.")
        name = input("Name:")


def read_guitar_file():
    in_file = open('guitars.csv', 'r')
    guitars = []
    for line in in_file:
        parts = line.strip().split(',')
        print(parts)
        guitars.append(Guitar(parts[0], int(parts[1]), float(parts[2])))
    return guitars


main()
