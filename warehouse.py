warehouse = {
    "A1": 120,
    "A2": 75,
    "B1": 43,
    "B2": 500
}

def check_stock(location):
    print(location, "has", warehouse[location], "products.")

def add_stock(location, amount):
    warehouse[location] = warehouse[location] + amount
    print("Stock updated successfully!")
    print(location, "now has", warehouse[location], "products.")

def remove_stock(location, amount):
    if warehouse[location] >= amount:
        warehouse[location] = warehouse[location] - amount
        print("Stock removed successfully!")
        print(location, "now has", warehouse[location], "products.")
    else:
        print("Not enough stock!")

def show_total_stock():
    total = 0
    for shelf in warehouse:
        total = total + warehouse[shelf]
    print("Total stock:", total)

def show_low_stock():
    for shelf in warehouse:
        if warehouse[shelf] < 100:
            print(shelf, "low stock!")

while True:
    print("\n========== Warehouse AI ==========")
    print("1. Check stock")
    print("2. Add stock")
    print("3. Remove stock")
    print("4. Show total stock")
    print("5. Show low stock")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        location = input("Enter shelf name: ")
        check_stock(location)

    elif choice == "2":
        location = input("Which shelf do you want to restock? ")
        amount = int(input("How many products do you want to add? "))
        add_stock(location, amount)

    elif choice == "3":
        location = input("Which shelf do you want to remove products from? ")
        amount = int(input("How many products do you want to remove? "))
        remove_stock(location, amount)
    

    elif choice == "4":
        show_total_stock()

    elif choice == "5":
        show_low_stock()

    elif choice == "6":
        print("Exiting Warehouse AI. Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")
        
