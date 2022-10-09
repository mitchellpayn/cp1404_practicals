import random

#
# 
# # NUMBERS = []
# # # lines = int(input("How many quick picks do you wish to generate?: "))
# # lines = 3
# # for i in range(0, lines+1):
# #     for j in range(6):
# #         repeat = False
# #         # for j in range(6):
# #         new_number = random.randint(1, 45)
# #         # print(NUMBERS)
# #
# #         while not repeat:
# #             if new_number in NUMBERS:
# #                 new_number = random.randint(1, 45)
# #             else:
# #                 NUMBERS[i+1][j+1] = new_number
# #                 repeat = True
# #
# #
# # print(NUMBERS)
# # print(len(NUMBERS))
# 
NUMBERS_PER_LINE = 6
MIN = 1
MAX = 45

number_of_lines = 2  # int(input("How many quick picks do you wish to generate?: "))
while number_of_lines <= 0:
    print("Enter a number greater then 0")
    number_of_lines = int(input("How many quick picks do you wish to generate?: "))

for i in range(number_of_lines):
    numbers = []
    for j in range(NUMBERS_PER_LINE):
        number = random.randint(MIN, MAX)
        while number in numbers:
            number = random.randint(MIN, MAX)
        numbers.append(number)
    numbers.sort()
    print(" ".join(f"{number:2}" for number in numbers))
