from typing import List
from models.product import Product

class OrderedProduct:
    def __init__(self,product:Product,requested_quantity:int) -> None:
        self.product =product
        self.requested_quantity= requested_quantity
        self.actual_price = requested_quantity*product.price
        self.offer_id = "N/A"
        self.net_price = self.actual_price
    

    def __str__(self) -> str:
        return "{} - {} - {} - {} - {} - {}".format(self.product.id,self.product.name,self.requested_quantity,self.product.price,self.offer_id,self.net_price)


class Order:

    def __init__(self) -> None:
        self.ordered_products:List[OrderedProduct] = []
    
    def add_product(self,new_ordered_product) -> None:
        self.ordered_products.append(new_ordered_product)
    
    def get_total(self) -> int:
        total = 0
        for product  in self.ordered_products:
            total += product.net_price
        return total
    