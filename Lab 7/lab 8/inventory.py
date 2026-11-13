from product import Product 
##INVENTORY CLASS##

class Inventory:
    def __init__(self):
        self.products:list[Product] = []

    #add products to the list
    def add_product(self,product):
        self.products.append(product)
    def remove_product(self, product_id: str):
        for product in self.products:
            if product.getID(product_id):
                self.products.remove(product)
                return True

        return False

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




def find_product(self, product_id: str) -> Product | None:
    for product in self.products:
        if product.getID(product_id):
            return product

    return None


