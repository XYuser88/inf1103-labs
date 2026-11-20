from product import Product
from discount import DiscountStrategy, NoDiscount


class OrderLine:
    def __init__(self, product: Product, quantity: int):

        if type(quantity) is not int or quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        self.product: Product = product
        self.quantity: int = quantity

    def calculate_subtotal(self) -> float:
        return self.product.price * self.quantity


class Order:
    def __init__(self, orderId: str,
                 discount: DiscountStrategy | None = None):

        self.order_id: str = orderId
        self.order_lines: list[OrderLine] = []

        self.discount = discount if discount is not None else NoDiscount()

    def set_discount(self, discount: DiscountStrategy) -> None:
        self.discount = discount

    def add_order_line(self, product: Product, quantity: int) -> None:
        line = OrderLine(product, quantity)
        self.order_lines.append(line)

    def calculate_total(self) -> float:
        total = 0

        for line in self.order_lines:
            total += line.calculate_subtotal()

        return self.discount.apply(total)