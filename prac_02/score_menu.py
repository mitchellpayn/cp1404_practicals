"""
Redone score menu using fuctions
"""

menu = """
(r) to run program
(q) to quit"""


def main():
    print(menu)
    response = input("Enter response: ")
    while response != "q":
        score = int(input("Enter score: "))
        result = determine_score_result(score)
        if result == "Invalid score" or result == "":
            print(f"{result}\nPlease enter a value between 0 and 100.")
        else:
            print(f"{result}",'*' * score)






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