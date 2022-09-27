total_cost = 0
number_of_items = int(input("Number of items:"))
while number_of_items >= 0:
    for i in range(0, number_of_items):
        item_price = float(input(f"Cost of item {i+1}:"))
        total_cost = total_cost + item_price
    if total_cost > 100:
        total_cost = total_cost - ( total_cost * 0.1)
    if number_of_items == 0:
        print("Invalid Number of Items")
    else:
        print(f"Total price for the {number_of_items} items is ${total_cost:.2f}")
    total_cost = 0
    number_of_items = int(input("Number of Items:"))
