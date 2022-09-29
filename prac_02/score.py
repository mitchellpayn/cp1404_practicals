"""
CP1404/CP5632 - Practical
Score status using functions
"""

import random

def main():
    score = float(input("Enter score: "))
    result = determine_score_result(score)
    print(f"Your result is {result}")
    score = random.randint(0, 100)
    result = determine_score_result(score)
    print(f"Your result is {result}")

def determine_score_result(score):
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


main()