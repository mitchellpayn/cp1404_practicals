"""
Request users name and writes it to a file.
"""
# TASK 1
name = input("Enter your name: ")
# name = "Mitchell"
out_file = open("name.txt", 'w')
print(f"Your name is {name}", file=out_file)
out_file.close()

# TASK 2
in_file = open("name.txt", 'r')
name = in_file.readline()
in_file.close()
print(f"{name}")

# TASK 3
in_file = open("numbers.txt")
number_one = int(in_file.readline())
number_two = int(in_file.readline())
in_file.close()
print(f"{number_one} + {number_two} = {number_one + number_two}")

# TASK 4
total = 0
in_file = open("numbers.txt")
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(f"Total = {total}")
