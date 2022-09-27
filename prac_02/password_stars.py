password_min_length = 5
password = input("enter password:")
while password != "q":
    if len(password) < password_min_length:
        print("Password not long enough")
    else:
        print('*' * len(password))
    password = input("enter password")