from abc import ABC, abstractmethod

## PRODUCT CLASS ##

class Product(ABC):
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
    
    @abstractmethod
    def get_fulfilment_info(self):
        pass
    
class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass


#Physical product class inheriting from Product class##

class physicalproduct(Product, CanBeShipped):
    def __init__(self, pid, name, price, stock, weight):
        super().__init__(pid, name, price, stock)
        self.weight = weight

    def display_information(self):
        super().display_information()
        print("Product Weight: ", self.weight, "kg")

    def get_fulfilment_info(self):
        return "Requires physical shipping."

    def calculate_shipping_cost(self):
        return self.weight * 5
    
    def append_Dict(self):
        data = super().append_Dict()
        data["Type"] = "physical"
        data["Weight"] = self.weight
        return data

#digital product class inheriting from Product class##

class digitalproduct(Product):
    def __init__(self, pid, name, price, stock, download_size):
        super().__init__(pid, name, price, stock)
        self.download_size = download_size

    def display_information(self):
        super().display_information()
        print("Download Size:", self.download_size, "MB")

    def get_fulfilment_info(self):
        return "This will be delivered digitally."
    
    def append_Dict(self):
        data = super().append_Dict()
        data["Type"] = "digital"
        data["Download_Size"] = self.download_size
        return data