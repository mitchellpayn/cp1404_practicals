"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
Practical 01 Temperatures using functions
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_C_to_F(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            # TODO: Write this section to convert F to C and display the result
            # Hint: celsius = 5 / 9 * (fahrenheit - 32)
            # Remove the "pass" statement when you are done. It's a placeholder.

            fahrenheit = float(input("fahrenheit: "))
            celsius = convet_F_to_C(fahrenheit)
            print("Result: {:.2f} F".format(celsius))

        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convet_F_to_C(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def convert_C_to_F(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()