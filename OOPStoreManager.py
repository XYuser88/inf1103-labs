import json
## PRODUCT CLASS ##

class Product:
    def __init__(self,pid,name, price, stock):
        self.__pid = pid
        self.__name = name
        self.__price = price
        self.__stock = stock

    #update stock of certain product
    def update_stock(self, new_stock):
        if isinstance(new_stock, int) and new_stock >= 0:
            self.__stock = new_stock
            print("Stock successfully updated.")
        else:
            print("Stock must be a non-negative integer.")

    #get id of certain product
    def getID(self,pid):
        return self.__pid == pid

    #display information for one product
    def display_information(self):
        print("\nProduct ID: ", self.__pid)
        print("Product Name: ", self.__name)
        print("Product Price: ", self.__price)
        print("Product Stock: ", self.__stock)

    def append_Dict(self):
        return {
            "PID":self.__pid,
            "Name": self.__name,
            "Price": self.__price,
            "Stock": self.__stock
        }


##INVENTORY CLASS##

class Inventory:

    def __init__(self):
        self.products=[]

    #add products to the list
    def add_product(self,product):
        self.products.append(product)

    #search for a product
    def search_product(self, pid):
        for product in self.products:
            if product.getID(pid):
                return product

        return None

    def display_all(self):
        if len(self.products)==0:
            print("inventory is empty")
            return
        for product in self.products:
            product.display_information()


#file loading and saving
def load_inventory():
    inventory = Inventory()

    try:
        with open("inventory.json", "r") as file:
            data = json.load(file)

        for item in data:
            product = Product(
                item["PID"],
                item["Name"],
                item["Price"],
                item["Stock"]
            )
            inventory.add_product(product)

        print("Inventory loaded.")

    except FileNotFoundError:
        print("initialising empty inventory")
    return inventory

def save_inventory(inventory):
    data=[]

    for product in inventory.products:
        data.append(product.append_Dict())

    with open("inventory.json", "w") as file:
        json.dump(data, file)

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
        if stock_string>0:
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

    product = Product(pid, name, price, stock)
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

 