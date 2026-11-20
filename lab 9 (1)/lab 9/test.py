import unittest
from unittest.mock import patch
from contextlib import redirect_stdout
from io import StringIO

from discount import (
    NoDiscount,
    PercentageDiscount,
    BulkDiscount,
    StudentDiscount
)

from product_factory import ProductFactory
from product import physicalproduct, digitalproduct
from order import Order, OrderLine
from supplier import Supplier
from inventory import Inventory
from main import get_positive_float, load_products


class Lab9Tests(unittest.TestCase):

    def setUp(self):
        self.supplier = Supplier(
            "S001", "Example Supplier", "test@gmail.com"
        )

        self.product = ProductFactory.create(
            "physical", "P100", "Desk",
            50, 10, self.supplier, weight=2
        )

    # TEST 1 - Discount strategies

    def test_discount_strategies(self):

        order = Order("O1")
        order.add_order_line(self.product, 5)

        self.assertEqual(order.calculate_total(), 250)

        order.set_discount(BulkDiscount(200, 20))
        self.assertEqual(order.calculate_total(), 230)

        order.set_discount(PercentageDiscount(10))
        self.assertEqual(order.calculate_total(), 225)

        order.set_discount(StudentDiscount())
        self.assertEqual(order.calculate_total(), 237.5)

        order.set_discount(NoDiscount())
        self.assertEqual(order.calculate_total(), 250)

    # TEST 2 - Sharing strategies

    def test_strategy_shared(self):

        discount = PercentageDiscount(10)

        order1 = Order("O1", discount)
        order2 = Order("O2", discount)

        self.assertIs(order1.discount, order2.discount)

    # TEST 3 - Product Factory

    def test_factory(self):

        physical = ProductFactory.create(
            "physical", "P001", "Laptop",
            1000, 10, self.supplier, weight=2
        )

        digital = ProductFactory.create(
            "digital", "D001", "Software",
            50, 10, self.supplier, download_size=100
        )

        self.assertIsInstance(physical, physicalproduct)
        self.assertIsInstance(digital, digitalproduct)

        with self.assertRaises(ValueError):
            ProductFactory.create(
                "service", "S001", "Service",
                50, 10, self.supplier
            )

    # TEST 4 - Validation

    def test_validation(self):

        with self.assertRaises(ValueError):
            ProductFactory.create(
                "physical", "P002", "Laptop",
                -100, 10, self.supplier
            )

        with self.assertRaises(ValueError):
            ProductFactory.create(
                "digital", "D002", "Software",
                0, 10, self.supplier
            )

        with self.assertRaises(ValueError):
            ProductFactory.create(
                "physical", "P003", "Chair",
                50, -5, self.supplier
            )

        with self.assertRaises(ValueError):
            self.product.update_stock(-5)

        with self.assertRaises(ValueError):
            OrderLine(self.product, 0)

        with self.assertRaises(ValueError):
            OrderLine(self.product, -1)

    # TEST 5 - Invalid user input

    def test_input_retry(self):

        with patch("builtins.input",
                   side_effect=["abc", "-5", "12.50"]):

            result = get_positive_float("Enter price: ")

        self.assertEqual(result, 12.50)

    # TEST 6 - CSV file loading

    def test_csv(self):

        inventory = Inventory()

        output = StringIO()

        with redirect_stdout(output):
            load_products(
                "products.csv",
                inventory,
                self.supplier
            )

        self.assertEqual(len(inventory.products), 3)
        self.assertIn("Skipping row 4", output.getvalue())
        self.assertIn("Skipping row 5", output.getvalue())
        self.assertIn("3 products loaded.", output.getvalue())

    # TEST 7 - Missing file

    def test_missing_file(self):

        inventory = Inventory()

        output = StringIO()

        with redirect_stdout(output):
            load_products(
                "missing.csv",
                inventory,
                self.supplier
            )

        self.assertEqual(len(inventory.products), 0)
        self.assertIn("Products file not found", output.getvalue())
        self.assertIn("Load attempt finished.", output.getvalue())


if __name__ == "__main__":
    unittest.main()