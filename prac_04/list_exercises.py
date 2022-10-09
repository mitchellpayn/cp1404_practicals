"""
List exercises
"""
numbers = []
for i in range(5):
    number = int(input(f"Number {i+1}: "))
    numbers.append(number)
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average number is {sum(numbers)/len(numbers)}")

user_names = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
names = []
# change user_names to all caps for comparing to user input
for i in user_names:
    names.append(i.upper())
user_name = input("Enter user name: ").upper()
if user_name in names:
    print("Access Granted")
else:
    print("Access Denied")

