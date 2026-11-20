from product import Product, physicalproduct, digitalproduct
from supplier import Supplier


class ProductFactory:

    @staticmethod
    def create(product_type: str, product_id: str,
               name: str, price: float, stock_quantity: int,
               supplier: Supplier, weight: float = 0.0,
               download_size: float = 0.0) -> Product:

        if product_type == "physical":
            return physicalproduct(
                product_id, name, price,
                stock_quantity, weight, supplier
            )

        elif product_type == "digital":
            return digitalproduct(
                product_id, name, price,
                stock_quantity, download_size, supplier
            )

        else:
            raise ValueError(f"Unknown product type: {product_type}")