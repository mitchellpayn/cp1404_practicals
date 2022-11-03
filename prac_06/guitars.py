"""
Get guitar info from user and display in meaningful manner.
"""
from guitar import Guitar


def main():
    guitars = []
    name = input("Name:")

    while name != "":
        year = int(input("Year:"))
        cost = float(input("Cost:"))
        guitar_to_add = [name, year, cost]
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost} added.")
        name = input("Name:")
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("The big boy", 1899, 200000.00))
    if guitars:
        guitars.sort()
        for i, guitar in enumerate(guitars):
            if guitar.is_vintage():
                vintage_string = "vintage"
            print(f"Guitar {i + 1}: {guitar.name:>20} ({guitar.year}), worth $ {guitar.cost:10,.2f} ({vintage_string})")


main()
