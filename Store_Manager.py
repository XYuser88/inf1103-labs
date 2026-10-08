import json

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


def display_all(): #display all products
    global inventory
    print("Current Inventory")
    for product in inventory:
        print("ID:", inventory['\tPID',],"\tName:",inventory["Name"],
              "\tPrice:",inventory["Price"],
              "\ttock:",inventory["Stock"])
    return 

def get_price():#get price via input and check validity
    print("Enter Product Price: ")


def add_product(get_product()): #add product to dictionary that is WITHIN a list, needs variable from an input function
    global inventory
    prod_id=input("Enter product ID: ")

    if prod_id=="":
        print("product ID cannot be empty.")
        return
    for product in inventory:
        if product ["Pid"]==prod_id:
            print("this product already exists.")
            return
        
    name=input("Enter product Name: ")
    if name=="":
        print("Name cannot be empty.")
        return
    Price=get_price()
    Stock=get_stock()

    return inventory

def get_product(): #input function to get product details input to append into add_products() functio

    return



variable=add_product("P004","ram stick",2400,10) #test variables
####  



def update_stock(PID,Stock_amt): #update stock in dictionary
     global products_list
     products_dictionary[PID]["Stock"]=Stock_amt
     return



def search_product(): #search for specific product in dictionary
     global products_list
     return










def load_inventory():#check whether inventory.txt exists, if not, initialise empty inventory=0
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


def Saveinventoryfile():
    global inventory
    with open("inventory.txt", 'w') as file:
        file.write('Inventory: ')
        file.write(str(inventory))
        file.write("\n")
        file.write("inventory list: \n")

        for transaction in inventorylist:
            file.write(str(transaction) +"\n")