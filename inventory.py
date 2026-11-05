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