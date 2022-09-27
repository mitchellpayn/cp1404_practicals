"""
menu script
"""
menu = """(H)ello
(G)oodbye
(Q)uit"""

name = str(input("Enter your name:"))
print(menu)
option = str(input("Select your option:\n"))
while option != "Q":
    if option == "H":
        print(f"Hello {name}\n")
    elif option == "G":
        print(f"Goodbye {name}\n")
    else:
        print("Invalid Option (Answer is case sensitive)\n")
    print(menu)
    option = str(input("Select your option:"))


