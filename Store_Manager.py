import json
def load_inventory():
    try:
        with open("inventory.json","r") as file:
            inventory = json.load(file)
            print(inventory)
        print("inventory loaded.")
            
    except FileNotFoundError: # only runs if error exists
        # insert new code to set inventory as 0 first
            inventory = []
            print(inventory)
            return inventory


# inventory=[
#      {"PID": "P001",
#       "Name":"Laptop",
#       "Price":1200,
#       "Stock":0},

#      {"PID": "P002",
#       "Name":"Mouse",
#       "Price":25.50,
#       "Stock":0},

#      {"PID": "P003",
#       "Name":"Keybaord",
#       "Price":1200,
#       "Stock":0},
# ]

def display_all(inventory): #display all products
    print("Current Inventory")
    for product in inventory:
        print("ID:", product['PID'],"\nName:",product["Name"],
              "\nPrice:",product["Price"],
              "\nStock:",product["Stock"])
    return 

def get_price():#get price via input and check validity
    price=input("Enter Product Price: ")
    dec_count=0
    if price=="":
        print("type the PRICE.")
        return
    elif price.isdigit==False:
        print("Enter either float or integer.")
    else:
        return float(price)

def get_stock():#get stock via input and check validity
    stock_string=input("Enter stock amount: ")

    if stock_string=="":
        print("Enter valid stock.")
        return
    if stock_string.isdigit():
        stock_string=int(stock_string)
        if stock_string>0:
            return stock_string
    print("Stock must be positive integer.")
    return False

def add_product(inventory): #add product to dictionary that is WITHIN a list, needs variable from an input function
    prod_id=input("Enter product ID: ")

    if prod_id=="":
        print("product ID cannot be empty.")
        return
    for product in inventory:#check if item exists
        if product ["PID"]==prod_id:
            print("this product already exists.")
            return
    else:
        name=input("Enter product Name: ")
        if name=="":
            print("Name cannot be empty.")
            return
        price=get_price()
        stock=get_stock()

        product={"PID": prod_id,
        "Name":name,
        "Price": price,
        "Stock":stock}
        inventory.append(product)

def search_product(inventory,prod_id): #search for specific product in dictionary
    for product in inventory:
        if product['PID']==prod_id:
            return product
    return None

def update_stock(inventory): #update stock in dictionary
    #ask product to update
    prod_id=input("Enter product ID: ")

    #search prod id
    product=search_product(inventory,prod_id)

    #check if product exist
    if product==None:
     print("Product not found.")
     return

    #show current stock
    print("Product: ", product["Name"])
    print("Current stock", product["Stock"])

    newStock=get_stock()

    product["Stock"]=newStock
    print("Stock successfully updated")


def Saveinventoryfile(inventory):
    with open("inventory.json", 'w') as file:
        json.dump(inventory,file)
    print("inventory saved.")

def menu():
    print("\n ======MENU========")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("--------------------------")

#main program
inventory=load_inventory()
while True:
    menu()
    option=input("Enter option: ")
    if option=="1":
        display_all(inventory)
    elif option=="2":
        add_product(inventory)
    elif option=="3":
        update_stock(inventory)
    elif option=="4":
        prod_id=input("Enter product ID you want to search: ")
        product = search_product(inventory, prod_id)
        if product is None:
            print("Error: Product not found.")
        else:
            display_all([product])
    elif option=="5":
        Saveinventoryfile(inventory)
    elif option=="6":
        Saveinventoryfile(inventory)
        print("Exiting program")
        break
    else:
        print("Invalid option.")




# print(inventory)
# add_product()
# print("==========================")

# print("==========================")
# print(inventory)
# update_stock()
# print(inventory)
