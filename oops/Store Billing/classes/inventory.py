from typing import Dict, List
from models.product import Product
from models.cart_item import CartItem

class Inventory:
    def __init__(self) -> None:
        self.products:Dict[any,Product] = {}

    def add_product(self,query)->None:
        
        query_props= query.split("|")
        prod_id,prod_name = int(query_props[0]),query_props[1]
        quantity,price = map(int,query_props[2:])

        new_product  = Product(prod_id,prod_name,quantity,price)        
        self.products[prod_id] = new_product
        print(new_product)
        print("Inventory updated.")

    
    def display_product_stock(self,prod_id)-> int:

        requested_product  = self.get_product(prod_id)
        print(requested_product.display_stock())


    def get_product(self,prod_id)-> Product:
        
        requested_product = self.products[prod_id]

        if requested_product is None:
            raise Exception("Product doesn't have in inventory")
        
        return requested_product
    
    def  reduce_quantity(self,cart:List[CartItem]):
        for cartItem  in cart:
            prod_id = cartItem.product.id
            self.products[prod_id].update_quantity(-cartItem.requested_quantity)
    