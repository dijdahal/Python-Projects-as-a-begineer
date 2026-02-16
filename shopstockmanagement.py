print("""
__        __  _____ _     ____ ___  __  __ _____ 
\ \      / / | ____| |   / ___/ _ \|  \/  | ____|
 \ \ /\ / /  |  _| | |  | |  | | | | |\/| |  _|  
  \ V  V /   | |___| |__| |__| |_| | |  | | |___ 
   \_/\_/    |_____|_____\____\___/|_|  |_|_____|
""")

shop_stock = {}


with open("inventory.txt", "r") as f:
    for line in f:
        clean_line = line.strip()
        parts = clean_line.split(",")
        name = parts[0]
        quantity = int(parts[1])

        shop_stock[name] = quantity

print("Inventory Loaded:", shop_stock)
while True:
    print("1. View Stock")
    print("2. Update")
    print("3. Exit")
    choice = int(input("Enter your Choice(1-3): "))
    if choice == 1:
        for items in shop_stock:
            print(f"{items}")
    elif choice == 2:
        item_name = input("Which item?").lower()
        if item_name in shop_stock:
            print("Do you want to")
            choice_two = input("(1) add or (2) remove?")
            if choice_two == "1":
                increase = int(input("How many item to add"))
                shop_stock[item_name] += increase
                print("Inventory Loaded:", shop_stock)
            elif choice_two == "2":
                decrease = int(input("How many item to remove"))
                shop_stock[item_name] -= decrease
                print("Inventory Loaded:", shop_stock)
    elif choice == 3:
        with open("inventory.txt", "w")as f:

            for name, quantity in shop_stock.items():
                f.write(f"{name},{quantity}\n")
        break
