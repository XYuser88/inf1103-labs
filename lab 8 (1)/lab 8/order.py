
from product import Product

# SECTION 4.1 - ORDERLINE CLASS

class OrderLine:
    def __init__(self, product: Product, quantity: int):
        self.product: Product = product
        self.quantity: int = quantity

    def calculate_subtotal(self) -> float:
        return self.product.price * self.quantity


# SECTION 4.2 - ORDER CLASS

class Order:
    def __init__(self, orderId: str):
        self.order_id: str = orderId
        self.order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        line = OrderLine(product, quantity)
        self.order_lines.append(line)

    def calculate_total(self) -> float:
        total = 0

        for line in self.order_lines:
            total += line.calculate_subtotal()

        return total
