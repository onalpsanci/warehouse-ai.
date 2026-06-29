import json
import os

warehouse = {
    "A1": {"product": "Laptop", "stock": 120},
    "A2": {"product": "Keyboard", "stock": 75},
    "B1": {"product": "Mouse", "stock": 43},
    "B2": {"product": "Monitor", "stock": 500}
}

def save_data():
    with open("warehouse.json", "w") as file:
        json.dump(warehouse, file, indent=4)

def load_data():
    global warehouse
    if os.path.exists("warehouse.json"):
        with open("warehouse.json", "r") as file:
            warehouse = json.load(file)

def check_stock(location):
    if location in warehouse:
        product = warehouse[location]["product"]
        stock = warehouse[location]["stock"]
        print(location, "contains", product, "with", stock, "units.")
    else:
        print("Shelf not found.")

def add_stock(location, amount):
    if location in warehouse:
        warehouse[location]["stock"] += amount
        save_data()
        print("Stock updated successfully!")
        print(location, "now has", warehouse[location]["stock"], "units.")
    else:
        print("Shelf not found.")

def remove_stock(location, amount):
    if location in warehouse:
        if warehouse[location]["stock"] >= amount:
            warehouse[location]["stock"] -= amount
            save_data()
            print("Stock removed successfully!")
            print(location, "now has", warehouse[location]["stock"], "units.")
        else:
            print("Not enough stock!")
    else:
        print("Shelf not found.")

def show_total_stock():
    total = 0
    for shelf in warehouse:
        total += warehouse[shelf]["stock"]
    print("Total stock:", total)

def show_low_stock():
    for shelf in warehouse:
        if warehouse[shelf]["stock"] < 100:
            print(shelf, "low stock!")

def add_new_product(location, product, stock):
    warehouse[location] = {
        "product": product,
        "stock": stock
    }
    save_data()
    print("New product added successfully!")

def delete_product(location):
    if location in warehouse:
        del warehouse[location]
        save_data()
        print("Product deleted successfully!")
    else:
        print("Shelf not found.")

def search_product(product_name):
    found = False

    for shelf in warehouse:
        if warehouse[shelf]["product"].lower() == product_name.lower():
            print("Product found!")
            print("Shelf:", shelf)
            print("Stock:", warehouse[shelf]["stock"])
            found = True
def show_statistics():
    total_shelves = len(warehouse)
    total_stock = 0

    highest_shelf = None
    lowest_shelf = None

    for shelf in warehouse:
        stock = warehouse[shelf]["stock"]
        total_stock += stock

        if highest_shelf is None or stock > warehouse[highest_shelf]["stock"]:
            highest_shelf = shelf

        if lowest_shelf is None or stock < warehouse[lowest_shelf]["stock"]:
            lowest_shelf = shelf

    average_stock = total_stock / total_shelves

    print("\n========== Warehouse Statistics ==========")
    print("Total shelves:", total_shelves)
    print("Total stock:", total_stock)
    print("Average stock:", average_stock)
    print("Highest stock:", warehouse[highest_shelf]["product"], "-", warehouse[highest_shelf]["stock"], "units")
    print("Lowest stock:", warehouse[lowest_shelf]["product"], "-", warehouse[lowest_shelf]["stock"], "units")
    if not found:
        print("Product not found.")

load_data()

while True:
    print("\n========== Warehouse AI ==========")
    print("1. Check stock")
    print("2. Add stock")
    print("3. Remove stock")
    print("4. Show total stock")
    print("5. Show low stock")
    print("6. Exit")
    print("7. Show all shelves")
    print("8. Add new product")
    print("9. Delete product")
    print("10. Search product")
    print("11. Warehouse statistics")
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

    elif choice == "7":
        print("\n===== Warehouse Report =====")
        for shelf in warehouse:
            print("Shelf:", shelf, "| Product:", warehouse[shelf]["product"], "| Stock:", warehouse[shelf]["stock"])

    elif choice == "8":
        location = input("Enter new shelf: ")
        product = input("Enter product name: ")
        stock = int(input("Enter stock amount: "))
        add_new_product(location, product, stock)

    elif choice == "9":
        location = input("Enter shelf to delete: ")
        delete_product(location)

    elif choice == "10":
        product = input("Enter product name: ")
        search_product(product)
    
    elif choice == "11":
        show_statistics()
    else:
        print("Invalid option. Please try again.")
    
