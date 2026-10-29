## PRODUCT CLASS ##

class product:
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
        return self.productID == pid

    #display information for one product
    def display_information(self):
        print("Product ID: ", self.__productID)
        print("Product Name: ", self.__name)
        print("Product Price: ", self.__price)
        print("Product Stock: ", self.__stock)

    def append_Dict(self):
        return {
            "PID":self.__productID,
            "Name": self.__name,
            "Price": self.__price,
            "Stock": self.__stock
        }


##INVENTORY CLASS##

class inventory:

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
