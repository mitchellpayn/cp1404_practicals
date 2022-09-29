"""
Get the right length password and print the length in *'s.
"""

def main():
    password = get_password()
    print_name_in_stars(password)


def print_name_in_stars(password):
    print('*' * len(password))


def get_password():
    password_min_length = 5
    password = input("enter password:")
    if len(password) < password_min_length:
        print("Password not long enough")
        password = input("enter password")
    return password


main()