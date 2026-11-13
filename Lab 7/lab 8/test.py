
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
print("Test 2.2: Can products still access their supplier after deleting the supplier variable?")

del supplier

laptop.display_information()
software.display_information()

assert laptop.supplier is software.supplier
print("PASS: Both products still reference the same supplier.")


# SECTION 3 - AGGREGATION
print("\n===== SECTION 3: AGGREGATION =====")
print("Test 3.2: Can a product be removed from Inventory A and transferred to Inventory B?")

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

assert inventory_A.find_product("P001") is None
assert inventory_B.find_product("P001") is laptop

print("PASS: Product transferred without being destroyed.")


# SECTION 4 - COMPOSITION
print("\n===== SECTION 4: COMPOSITION =====")
print("Test 4.1: Does OrderLine calculate the correct subtotal?")
print("Test 4.2: Does Order calculate the correct total?")

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

assert order1.calculate_total() == 2050
assert order2.calculate_total() == 3000

print("PASS: Order totals are correct.")

print("\nTest 4.3: Do two orders create separate OrderLines for the same Product?")

print(
    "Same Product?",
    order1.order_lines[0].product is order2.order_lines[0].product
)

print(
    "Same OrderLine?",
    order1.order_lines[0] is order2.order_lines[0]
)

assert order1.order_lines[0].product is order2.order_lines[0].product
assert order1.order_lines[0] is not order2.order_lines[0]

print("PASS: Orders have separate OrderLines but share the Product.")

print("\nTest 4.3: Does the Product remain usable after deleting an Order variable?")

temporary_order = Order("O003")
temporary_order.add_order_line(laptop, 1)

print("Temporary order lines:", len(temporary_order.order_lines))

del temporary_order

laptop.display_information()

print("PASS: Product remains usable after deleting the Order variable.")


# SECTION 6 - LISKOV SUBSTITUTION PRINCIPLE
print("\n===== SECTION 6: LSP =====")
print("Test 6.2: Can the same function accept both PhysicalProduct and DigitalProduct?")

def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())

show_product_details(laptop)
show_product_details(software)

print("PASS: Both subclasses work with the same Product function.")


# SECTION 7 - POLYMORPHISM
print("\n===== SECTION 7: POLYMORPHISM =====")
print("Test 7.2: Do different Product subclasses produce their own fulfilment information?")

inventory = Inventory()

inventory.add_product(laptop)
inventory.add_product(software)

for product in inventory.products:
    product.display_information()
    print(product.get_fulfilment_info())

assert laptop.get_fulfilment_info() == "Requires physical shipping."
assert software.get_fulfilment_info() == "This will be delivered digitally."

print("PASS: Both subclasses provide their own fulfilment information.")


# SECTION 9 - TESTING AND REVIEW
print("\n===== SECTION 9: TESTING AND REVIEW =====")
print("Test 9: Verify inventory, order calculations and product behaviour.")

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

print("PASS: All automated assertions passed.")
