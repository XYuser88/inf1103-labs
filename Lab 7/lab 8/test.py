
from supplier import Supplier
from product import physicalproduct
from inventory import Inventory

# Create supplier and laptop
supplier = Supplier("S001", "ABC Supplies", "abc@gmail.com")
laptop = physicalproduct("P001", "Laptop", 1000, 5, 2.5, supplier)

# Create two inventories
inventory_A = Inventory()
inventory_B = Inventory()

# Add laptop to Inventory A
inventory_A.add_product(laptop)

# Remove laptop from Inventory A
inventory_A.remove_product("P001")

# Add the SAME laptop to Inventory B
inventory_B.add_product(laptop)

# Check both inventories
print("Inventory A:")
inventory_A.display_all()

print("\nInventory B:")
inventory_B.display_all()

# Check laptop still exists
print("\nOriginal laptop:")
laptop.display_information()
