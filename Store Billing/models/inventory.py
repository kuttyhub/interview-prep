from typing import Dict
from models.product import Product

class Inventory:
    def __init__(self) -> None:
        self.products:Dict[any,Product] = {}

    def add_product(self,product:Product)->None:
        self.products[product.id] = product
    
    def get_product(self,prod_id)-> Product:
        
        requested_product = self.products[prod_id]

        if requested_product is None:
            raise Exception("Product doesn't have in inventory")
        
        return requested_product
    