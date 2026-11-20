import math 
from abc import ABC, abstractmethod
from supplier import Supplier

## PRODUCT CLASS ##

class Product(ABC):
    def __init__(self, pid: str, name: str, price: float,
                 stock: int, supplier: Supplier) -> None:

        if not math.isfinite(price) or price <= 0:
            raise ValueError("Price must be greater than zero.")

        if type(stock) is not int or stock < 0:
            raise ValueError("Stock must be a non-negative integer.")

        self.__pid = pid
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.supplier: Supplier = supplier

    #update stock of certain product
    def update_stock(self, new_stock: int) -> None:

        if type(new_stock) is not int or new_stock < 0:
            raise ValueError("Stock must be a non-negative integer.")

        self.__stock = new_stock
        print("Stock successfully updated.")


    # Get ID of certain product
    def getID(self, pid: str) -> bool:

        return self.__pid == pid

    @property
    def price(self) -> float:
        return self.__price



    #display information for one product
    def display_information(self) -> None:
        print("\nProduct ID: ", self.__pid)
        print("Product Name: ", self.__name)
        print("Product Price: ", self.__price)
        print("Product Stock: ", self.__stock)
        self.supplier.display_information()

    def append_Dict(self) -> dict[str, str | int | float | dict[str, str]]:
        return {
        "PID": self.__pid,
        "Name": self.__name,
        "Price": self.__price,
        "Stock": self.__stock,
        "Supplier": {
            "supplier_id": self.supplier.supplier_id,
            "name": self.supplier.name,
            "contact_email": self.supplier.contact_email
        }
    }

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass

#Physical product class inheriting from Product class##

class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self) -> float:
        pass

class physicalproduct(Product, CanBeShipped):
    def __init__(self, pid: str, name: str, price: float,
                 stock: int, weight: float, supplier: Supplier) -> None:
        super().__init__(pid, name, price, stock, supplier)
        self.weight: float = weight

    def display_information(self) -> None:
        super().display_information()
        print("Product Weight: ", self.weight, "kg")

    def get_fulfilment_info(self) -> str:
        return "Requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        return self.weight * 5

    def append_Dict(self) -> dict[str, str | int | float | dict[str, str]]:
        data = super().append_Dict()
        data["Type"] = "physical"
        data["Weight"] = self.weight
        return data

#digital product class inheriting from Product class##


class digitalproduct(Product):
    def __init__(self, pid: str, name: str, price: float,
                 stock: int, download_size: float, supplier: Supplier) -> None:
        super().__init__(pid, name, price, stock, supplier)
        self.download_size: float = download_size

    def display_information(self) -> None:
        super().display_information()
        print("Download Size:", self.download_size, "MB")

    def get_fulfilment_info(self) -> str:
        return "This will be delivered digitally."

    def append_Dict(self) -> dict[str, str | int | float | dict[str, str]]:
        data = super().append_Dict()
        data["Type"] = "digital"
        data["Download_Size"] = self.download_size
        return data
