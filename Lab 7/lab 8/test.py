
from supplier import Supplier
from product import Product, physicalproduct, digitalproduct
from inventory import Inventory
from order import Order

# Create supplier and products
supplier = Supplier("S001", "ABC Supplies", "abc@gmail.com")

laptop = physicalproduct(
    "P001", "Laptop", 1000, 5, 2.5, supplier
)

software = digitalproduct(
    "P002", "Software", 50, 10, 500, supplier
)


# SECTION 2 - ASSOCIATION
print("\n===== SECTION 2: ASSOCIATION =====")

del supplier

laptop.display_information()
software.display_information()

print("Both products can still access their supplier.")


# SECTION 3 - AGGREGATION
print("\n===== SECTION 3: AGGREGATION =====")

inventory_A = Inventory()
inventory_B = Inventory()

inventory_A.add_product(laptop)

print("\nInventory A before removal:")
inventory_A.display_all()

inventory_A.remove_product("P001")

print("\nInventory A after removal:")
inventory_A.display_all()

print("\nProduct still exists:")
laptop.display_information()

inventory_B.add_product(laptop)

print("\nInventory B after transfer:")
inventory_B.display_all()


# SECTION 4 - COMPOSITION
print("\n===== SECTION 4: COMPOSITION =====")

order1 = Order("O001")
order2 = Order("O002")

order1.add_order_line(laptop, 2)
order1.add_order_line(software, 1)

order2.add_order_line(laptop, 3)

print("\nOrder 1:")
for line in order1.order_lines:
    line.product.display_information()
    print("Quantity:", line.quantity)
    print("Subtotal:", line.calculate_subtotal())

print("Order 1 total:", order1.calculate_total())
print("Order 2 total:", order2.calculate_total())

print(
    "Same Product?",
    order1.order_lines[0].product is order2.order_lines[0].product
)

print(
    "Same OrderLine?",
    order1.order_lines[0] is order2.order_lines[0]
)


# SECTION 6 - LISKOV SUBSTITUTION PRINCIPLE
print("\n===== SECTION 6: LSP =====")

def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())

show_product_details(laptop)
show_product_details(software)


# SECTION 7 - POLYMORPHISM
print("\n===== SECTION 7: POLYMORPHISM =====")

inventory = Inventory()

inventory.add_product(laptop)
inventory.add_product(software)

for product in inventory.products:
    product.display_information()
    print(product.get_fulfilment_info())


# SECTION 9 - TESTING AND REVIEW
print("\n===== SECTION 9: TEST RESULTS =====")

assert inventory_A.find_product("P001") is None
assert inventory_B.find_product("P001") is laptop

assert order1.calculate_total() == 2050
assert order2.calculate_total() == 3000

assert order1.order_lines[0].product is order2.order_lines[0].product
assert order1.order_lines[0] is not order2.order_lines[0]

assert laptop.get_fulfilment_info() == "Requires physical shipping."
assert software.get_fulfilment_info() == "This will be delivered digitally."

assert inventory.find_product("P001") is laptop
assert inventory.find_product("P002") is software

print("All automated assertions passed.")
