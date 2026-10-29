## PRODUCT CLASS ##

class product:
    def __init__(self,pid,name, price, stock):
        self.__pid = pid
        self.__name = name
        self.__price = price
        self.__stock = stock

    def update_stock(self, new_stock):
        if isinstance(new_stock, int) and new_stock >= 0:
            self.__stock = new_stock
            print("Stock successfully updated.")
        else:
            print("Stock must be a non-negative integer.")

    def getID(self,pid):
        return self.productID == pid

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
    
    

