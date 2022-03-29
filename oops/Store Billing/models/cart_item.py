from models.product import Product

class CartItem:
    def __init__(self,product:Product,requested_quantity:int) -> None:
        self.product =product
        self.requested_quantity= requested_quantity
        self.actual_price = requested_quantity*product.price
        self.offer_id = None
        self.net_price = self.actual_price
    
    def __format_offer_id(self) -> str:
        return "N/A" if self.offer_id == None else str(self.offer_id)

    def __str__(self) -> str:
        return f"{self.product.id} - {self.product.name} - {self.requested_quantity} - {self.product.price} - {self.__format_offer_id()} - {self.net_price}"
