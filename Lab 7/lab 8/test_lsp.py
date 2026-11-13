
from supplier import Supplier
from product import Product, physicalproduct, digitalproduct

def show_product_details(product: Product):
    product.display_information()
    print(product.get_fulfilment_info())

supplier = Supplier("S001", "ABC Supplies", "abc@gmail.com")

laptop = physicalproduct("P001", "Laptop", 1000, 5, 2.5, supplier)
software = digitalproduct("P002", "Software", 50, 10, 500, supplier)

show_product_details(laptop)
show_product_details(software)
