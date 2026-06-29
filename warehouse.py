import json
import os
from datetime import datetime
import csv


warehouse = {
    "A1": {"product": "Laptop", "stock": 120, "price": 1200, "min_stock": 20},
    "A2": {"product": "Keyboard", "stock": 75, "price": 80, "min_stock": 30},
    "B1": {"product": "Mouse", "stock": 43, "price": 30, "min_stock": 50},
    "B2": {"product": "Monitor", "stock": 500, "price": 250, "min_stock": 40}
}

def save_data():
    with open("warehouse.json", "w") as file:
        json.dump(warehouse, file, indent=4)

def load_data():
    global warehouse
    if os.path.exists("warehouse.json"):
        with open("warehouse.json", "r") as file:
            warehouse = json.load(file)

def log_action(action):
    with open("logs.txt", "a") as file:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(time + " - " + action + "\n")

def check_stock(location):
    if location in warehouse:
        item = warehouse[location]
        print(location, "contains", item["product"], "| Stock:", item["stock"], "| Price: $", item.get("price", 0))
    else:
        print("Shelf not found.")

def add_stock(location, amount):
    if location in warehouse:
        warehouse[location]["stock"] += amount
        save_data()
        log_action("Added " + str(amount) + " units to " + location)
        print("Stock updated successfully!")
    else:
        print("Shelf not found.")

def remove_stock(location, amount):
    if location in warehouse:
        if warehouse[location]["stock"] >= amount:
            warehouse[location]["stock"] -= amount
            save_data()
            log_action("Removed " + str(amount) + " units from " + location)
            print("Stock removed successfully!")
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

def add_new_product(location, product, stock, price, min_stock):
    warehouse[location] = {
        "product": product,
        "stock": stock,
        "price": price,
        "min_stock": min_stock
    }
    save_data()
    log_action("Added new product " + product + " to shelf " + location)
    print("New product added successfully!")

def delete_product(location):
    if location in warehouse:
        product = warehouse[location]["product"]
        del warehouse[location]
        save_data()
        log_action("Deleted product " + product + " from shelf " + location)
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
            print("Price: $", warehouse[shelf].get("price", 0))
            found = True

    if not found:
        print("Product not found.")

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

def show_restock_recommendations():
    print("\n===== Restock Recommendations =====")
    found = False

    for shelf in warehouse:
        stock = warehouse[shelf]["stock"]
        min_stock = warehouse[shelf].get("min_stock", 0)

        if stock < min_stock:
            print("Shelf:", shelf, "| Product:", warehouse[shelf]["product"], "| Stock:", stock, "| Minimum Stock:", min_stock, "| Recommendation: Reorder")
            found = True

    if not found:
        print("All products are above minimum stock levels.")

def show_warehouse_value():
    total_value = 0
    print("\n===== Warehouse Value Report =====")

    for shelf in warehouse:
        item = warehouse[shelf]
        value = item["stock"] * item.get("price", 0)
        total_value += value
        print("Shelf:", shelf, "| Product:", item["product"], "| Value: $", value)

    print("Total warehouse value: $", total_value)
def export_to_csv():
    with open("warehouse_report.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Shelf",
            "Product",
            "Stock",
            "Price",
            "Minimum Stock"
        ])

        for shelf in warehouse:
            item = warehouse[shelf]

            writer.writerow([
                shelf,
                item["product"],
                item["stock"],
                item.get("price", 0),
                item.get("min_stock", 0)
            ])

    log_action("Exported warehouse report to CSV")
    print("Warehouse exported successfully!")

def edit_product(location, new_product, new_price, new_min_stock):
    if location in warehouse:
        warehouse[location]["product"] = new_product
        warehouse[location]["price"] = new_price
        warehouse[location]["min_stock"] = new_min_stock

        save_data()
        log_action("Updated product on shelf " + location)
        print("Product updated successfully!")
    else:
        print("Shelf not found.")
def show_all_shelves():
    print("\n===== Warehouse Report =====")
    for shelf in warehouse:
        item = warehouse[shelf]
        print("Shelf:", shelf, "| Product:", item["product"], "| Stock:", item["stock"], "| Price: $", item.get("price", 0), "| Min Stock:", item.get("min_stock", 0))

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
    print("12. Restock recommendations")
    print("13. Warehouse value report")
    print("14. Export to CSV")
    print("15. Edit product")

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
        show_all_shelves()

    elif choice == "8":
        location = input("Enter new shelf: ")
        product = input("Enter product name: ")
        stock = int(input("Enter stock amount: "))
        price = float(input("Enter product price: "))
        min_stock = int(input("Enter minimum stock level: "))
        add_new_product(location, product, stock, price, min_stock)

    elif choice == "9":
        location = input("Enter shelf to delete: ")
        delete_product(location)

    elif choice == "10":
        product = input("Enter product name: ")
        search_product(product)

    elif choice == "11":
        show_statistics()

    elif choice == "12":
        show_restock_recommendations()

    elif choice == "13":
        show_warehouse_value()
    
    elif choice == "14":
        export_to_csv()
    
    elif choice == "15":
        location = input("Enter shelf to edit: ")
        new_product = input("Enter new product name: ")
        new_price = float(input("Enter new price: "))
        new_min_stock = int(input("Enter new minimum stock level: "))

        edit_product(location, new_product, new_price, new_min_stock)
    
    else:
        print("Invalid option. Please try again.")