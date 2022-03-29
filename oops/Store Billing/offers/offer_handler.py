from order import Order
from offers.product_offer import ProductOfferHandler
from offers.multi_product_offer import MultiProductHandler


class OffersHandler:
    def __init__(self) -> None:
        self.product_handler = ProductOfferHandler()
        self.multi_product_handler = MultiProductHandler()

    def add_new_product_offer(self,new_offer):
        self.product_handler.add_new_offer(new_offer)

    def add_new_multi_product_offer(self,new_offer):
        self.multi_product_handler.add_new_offer(new_offer)
    
    def apply_all_offers(self,order:Order):
        order = self.multi_product_handler.apply_offer(order)
        order = self.product_handler.apply_offer(order)

        return order
