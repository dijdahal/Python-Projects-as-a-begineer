expenses = []
while True:

    name = input("Enter the item name: ")
    if name.lower() == 'done':
        break
    price = float(input("Enter the Price of item: "))
    category = input("Enter the category of item: ")
    expense = {
        "item": name,
        "price": price,
        "category": category

    }
    expenses.append(dict)
    print("Item added!!!")
    print(expenses)
    only_price = [p["price"] for p in expenses]
    sum(only_price)
    expensive_items=[p["price"] for p in expenses if p >100]