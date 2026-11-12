
from supplier import Supplier
from product import physicalproduct, digitalproduct

# Create supplier
supplier = Supplier("S001", "123 Supplies", "123@gmail.com")

# Create two products using the same supplier
laptop = physicalproduct("P001", "Laptop", 1000, 5, 2.5, supplier)
software = digitalproduct("P002", "Software", 50, 10, 500, supplier)

# Delete supplier variable
del supplier

# Check whether products can still access supplier
laptop.display_information()
software.display_information()
