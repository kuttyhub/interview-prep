from classes.order import Order
from classes.offers.product_offer import ProductOfferHandler
from classes.offers.multi_product_offer import MultiProductHandler
from models.offer_handller import OfferHandler

class OffersHandler:
    def __init__(self) -> None:
        self.product_offer_handler = ProductOfferHandler()
        self.multi_product_offer_handler = MultiProductHandler()
        
        self.offer_handlers={}
        self.offer_handlers[1]=self.product_offer_handler
        self.offer_handlers[2]=self.multi_product_offer_handler

    def add_new_offer(self, query):
        offer_type = int(query.split("|")[-1])
        offer_handler:OfferHandler =self.offer_handlers[offer_type]
        offer_handler.add_new_offer(query)
    

    def apply_all_offers(self,order:Order):

        order = self.multi_product_offer_handler.apply_offer(order)
        order = self.product_offer_handler.apply_offer(order)
        return order
