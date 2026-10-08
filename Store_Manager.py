import json
def load_inventory():
    global inventory,inventorylist
    try:
        with open("inventory.txt","r") as file:
            transaction = file.readlines()
            inventory = int(transaction[0].split(": ")[1])

            for transaction in transaction[2:]:
                inventorylist.append(int(transaction))
            print(inventory)
            
    except FileNotFoundError: # only runs if error exists
        # insert new code to set inventory as 0 first
            inventory = 0
            print(inventory)

inventory=[
     {"PID": "P001",
      "Name":"Laptop",
      "Price":1200,
      "Stock":0},

     {"PID": "P002",
      "Name":"Mouse",
      "Price":25.50,
      "Stock":0},

     {"PID": "P003",
      "Name":"Keybaord",
      "Price":1200,
      "Stock":0},
]

def display_all(inventory=inventory): #display all products
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

    if stock_string.isdigit():
        stock_string=int(stock_string)
        if stock_string>0:
            return stock_string
    print("Stock must be positive integer.")
    return False

def add_product(inventory=inventory): #add product to dictionary that is WITHIN a list, needs variable from an input function
    prod_id=input("Enter product ID: ")

    if prod_id=="":
        print("product ID cannot be empty.")
        return
   
    for product in inventory:#check if item exists
        if product ["PID"]==prod_id:
            print("this product already exists.")
            return
        
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

def search_product(inventory=inventory,prod_id=inventory): #search for specific product in dictionary
    for product in inventory:
        if product['PID']==prod_id:
            return product
    return None

def update_stock(inventory=inventory): #update stock in dictionary
    #ask product to update
    prod_id=input("Enter product ID: ")

    #search prod id
    product=search_product(inventory,prod_id)

    #check if product exist
    if product==None:
     print("Product not found.")
     return

def Saveinventoryfile(inventory):
    with open("inventory.json", 'w') as file:
        json.dump(inventory,file)
    print("inventory saved.")

# print(inventory)
# add_product()
# print("==========================")
print(inventory)
product_id=input("Enter product ID you want to search: ")
product = search_product(inventory, product_id)
if product is None:
    print("Error: Product not found.")
else:
    display_all([product])
