numbers = [3, 1, 4, 1, 5, 9, 2]
# numbers[0] #3
# numbers[-1] #2
# numbers[3] #1
# numbers[:-1] #2       [3, 1, 4, 1, 5, 9] - values up to -1 value
# numbers[3:4] #1, 5    1 - doesn't include the end value
# 5 in numbers #1       True
# 7 in numbers #0       False
# "3" in numbers #False
# numbers + [6, 5, 3] # [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
numbers[0] = "10"
numbers[-1] = 1
print(numbers)
for number in range(2, len(numbers)):
    print(numbers[number])
if 9 in numbers:
    print("9 is in numbers")
else:
    print("9 is not in numbers")
