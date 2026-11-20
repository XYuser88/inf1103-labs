import json
import csv
import math
from product_factory import ProductFactory
from inventory import Inventory
from supplier import Supplier


# FILE LOADING AND SAVING

def load_inventory():
    inventory = Inventory()

    try:
        with open("inventory.json", "r") as file:
            data = json.load(file)

        for item in data:
            try:
                supplier_data = item["Supplier"]

                supplier = Supplier(
                    supplier_data["supplier_id"],
                    supplier_data["name"],
                    supplier_data["contact_email"]
                )

                product = ProductFactory.create(
                    item["Type"],
                    item["PID"],
                    item["Name"],
                    item["Price"],
                    item["Stock"],
                    supplier,
                    weight=item.get("Weight", 0.0),
                    download_size=item.get("Download_Size", 0.0)
                )

                inventory.add_product(product)

            except (ValueError, KeyError, TypeError) as error:
                print(f"Skipping invalid inventory entry: {error}")

        print("Inventory loaded.")

    except FileNotFoundError:
        print("Initialising empty inventory.")

    except json.JSONDecodeError as error:
        print(f"Invalid inventory JSON: {error}")
        raise SystemExit(1)

    return inventory


def save_inventory(inventory):
    data = []

    for product in inventory.products:
        data.append(product.append_Dict())

    with open("inventory.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Inventory is saved.")


# INPUT VALIDATION

def get_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))

            if not math.isfinite(value) or value <= 0:
                print("Please enter a number greater than zero.")
                continue

            return value

        except ValueError:
            print("Please enter a valid number, e.g. 12.50")


def get_price():
    return get_positive_float("Enter Product Price: ")


def get_stock():
    while True:
        try:
            stock = int(input("Enter stock amount: "))

            if stock < 0:
                print("Stock must be a non-negative integer.")
                continue

            return stock

        except ValueError:
            print("Stock must be a non-negative integer.")


# SECTION 5.2 - CSV FILE LOADING

def load_products(path: str, inventory: Inventory,
                  supplier: Supplier) -> None:

    loaded = 0

    try:
        file = open(path, newline="", encoding="utf-8")

    except FileNotFoundError:
        print(f"Products file not found: {path}")

    except OSError as error:
        print(f"Unable to open products file: {error}")

    else:
        with file:
            rows = csv.reader(file)
            next(rows, None)

            for row_number, row in enumerate(rows, start=2):
                try:
                    product_type, pid, name, price, stock = row

                    product = ProductFactory.create(
                        product_type,
                        pid,
                        name,
                        float(price),
                        int(stock),
                        supplier
                    )

                    if inventory.search_product(pid) is not None:
                        raise ValueError(f"Duplicate product ID: {pid}")

                    inventory.add_product(product)
                    loaded += 1

                except ValueError as error:
                    print(f"Skipping row {row_number}: {error}")

        print(f"{loaded} products loaded.")

    finally:
        print("Load attempt finished.")


# ADD PRODUCT

def product_input(inventory: Inventory) -> None:

    print("\nAdd Inventory")

    pid = input("Enter Product ID: ").strip()

    if not pid:
        print("Product ID cannot be empty.")
        return

    if inventory.search_product(pid) is not None:
        print("Product already exists.")
        return

    name = input("Enter Product Name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    price = get_price()
    stock = get_stock()

    product_type = input(
        "Type (1 = Physical, 2 = Digital): "
    ).strip()

    if product_type not in ("1", "2"):
        print("Invalid product type.")
        return

    supplier_id = input("Enter Supplier ID: ")
    supplier_name = input("Enter Supplier Name: ")
    supplier_email = input("Enter Supplier Email: ")

    if not supplier_id.strip() or not supplier_name.strip() or not supplier_email.strip():
        print("Supplier information cannot be empty.")
        return

    supplier = Supplier(
        supplier_id,
        supplier_name,
        supplier_email
    )

    try:
        if product_type == "1":

            weight = float(input("Enter weight (kg): "))

            if weight < 0:
                print("Weight cannot be negative.")
                return

            product = ProductFactory.create(
                "physical", pid, name, price,
                stock, supplier, weight=weight
            )

        else:

            download_size = float(
                input("Enter download size (MB): ")
            )

            if download_size < 0:
                print("Download size cannot be negative.")
                return

            product = ProductFactory.create(
                "digital", pid, name, price,
                stock, supplier,
                download_size=download_size
            )

    except ValueError as error:
        print(error)
        return

    inventory.add_product(product)
    print("\nProduct Added Successfully!")


# UPDATE STOCK

def update_stock(inventory):

    pid = input("Enter product ID: ")
    product = inventory.search_product(pid)

    if product is None:
        print("Product not found.")
        return

    product.display_information()

    new_stock = get_stock()

    product.update_stock(new_stock)


# MENU

def menu():

    print("\n====== MENU ======")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("7. Import products.csv")
    print("--------------------------")


# MAIN PROGRAM

def main():

    inventory = load_inventory()

    while True:

        menu()
        option = input("Enter option: ")

        if option == "1":
            inventory.display_all()

        elif option == "2":
            product_input(inventory)

        elif option == "3":
            update_stock(inventory)

        elif option == "4":

            pid = input("Enter product ID you want to search: ")
            product = inventory.search_product(pid)

            if product is None:
                print("Error: Product not found.")

            else:
                product.display_information()

        elif option == "5":
            save_inventory(inventory)

        elif option == "6":
            save_inventory(inventory)
            inventory.display_all()
            print("Exiting program")
            break

        elif option == "7":

            supplier = Supplier(
                "CSV001",
                "CSV Supplier",
                ""
            )

            load_products(
                "products.csv",
                inventory,
                supplier
            )

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()