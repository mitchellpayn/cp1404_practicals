"""

"""


def main():
    emails_to_names = {}
    email_address = get_email()
    name = check_name(email_address)
    response = input(f"Is your name {name}? (Y/n): ")
    if response == "n":
        name = input("Enter you name: ")
        print(f"Name: {name}")


def get_email():
    email_address = input("Enter Email Address: ")
    return email_address


def check_name(email_address):
    address_split = email_address.split("@")
    name = address_split[0].split(".")
    name = " ".join(name).title()
    return name


main()
