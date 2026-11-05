import json
from product import Product, physicalproduct, digitalproduct
from inventory import Inventory


#file loading and saving
def load_inventory():
    inventory = Inventory()

    try:
        with open("inventory.json", "r") as file:
            data = json.load(file)

        for item in data:
            if item.get("Type") == "physical":
                product = physicalproduct(
                    item["PID"],
                    item["Name"],
                    item["Price"],
                    item["Stock"],
                    item["Weight"]
                )

            elif item.get("Type") == "digital":
                product = digitalproduct(
                    item["PID"],
                    item["Name"],
                    item["Price"],
                    item["Stock"],
                    item["Download_Size"]
                )

            else:
                print("Skipping unknown product type.")
                continue

            inventory.add_product(product)

        print("Inventory loaded.")

    except FileNotFoundError:
        print("Initialising empty inventory.")

    return inventory


def save_inventory(inventory):
    data = []

    for product in inventory.products:
        data.append(product.append_Dict())

    with open("inventory.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Inventory is saved.")

#input validation

def get_price():#get price via input and check validity
    price=input("Enter Product Price: ")
    
    if price=="":
        print("type the PRICE.")
        return
    try:
        price = float(price)

        if price < 0:
            print("price cannot be negative")
            return None

        return price

    except ValueError:
        print("Enter either float or integer.")
        return None

def get_stock():#get stock via input and check validity
    stock_string=input("Enter stock amount: ")

    if stock_string=="":
        print("Enter valid stock.")
        return
    if stock_string.isdigit():
        stock_string=int(stock_string)
        if stock_string>=0:
            return stock_string
    print("Stock must be positive integer.")
    return None

def product_input(inventory):
    pid = input("Enter product ID: ")
    if pid == "":
        print("product ID cannot be empty.")
        return

    product=inventory.search_product(pid)

    if product is not None:
        print("product already exists. ")
        return
    name = input("enter product name: ")
    if name=="":
        print("Name cannot be empty.")
        return
    
    price=get_price()
    stock=get_stock()

    if price is None or stock is None:
        return

    product_type = input("Physical or Digital? (p/d): ")

    if product_type == "p":
        try:
            weight = float(input("Enter weight (kg): "))
        except ValueError:
            print("Weight must be a number.")
            return
        
        if weight < 0:
            print("weight cannot be negative")
            return
        product = physicalproduct(pid, name, price, stock, weight)
    elif product_type == "d":
        try:
            download_size = float(input("Enter download size (MB): "))
        except ValueError:
            print("Download size must be a number.")
            return
        if download_size < 0:
            print("Download size cannot be negative.")
            return
        product = digitalproduct(pid, name, price, stock, download_size)

    else:
        print("Invalid product type.")
        return
    
    inventory.add_product(product)

    print("Product successfully added.")


def update_stock(inventory):
    pid= input("enter product ID:")
    product= inventory.search_product(pid)

    if product == None:
        print("product not found")
        return
    else:
        product.display_information()

    new_stock=get_stock()
    if new_stock==None:
        return
    else:
        product.update_stock(new_stock)

    


def menu():
    print("\n====== MENU ======")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("--------------------------")

#main program

inventory= load_inventory()
while True:
    menu()
    option=input("Enter option: ")
    if option=="1":
        inventory.display_all()
    elif option=="2":
        product_input(inventory)
    elif option=="3":
        update_stock(inventory)
    elif option=="4":
        pid=input("Enter product ID you want to search: ")
        product = inventory.search_product(pid)
        if product is None:
            print("Error: Product not found.")
        else:
            product.display_information()
    elif option=="5":
        save_inventory(inventory)
        print("Inventory saved.")
    elif option=="6":
        save_inventory(inventory)
        inventory.display_all()
        print("Exiting program")
        break
    else:
        print("Invalid option.")