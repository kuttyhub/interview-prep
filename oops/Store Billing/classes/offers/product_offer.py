from collections import defaultdict
from typing import Dict, List
from models.offer_handller import OfferHandler

from models.product_offer import ProductOffer
from classes.order import Order 


# "NEW-OFFER=>OFFER-NAME|OFFER-ID|Product-ID,Product-ID..|Minimum-Quantity|Discount-Percentage|offer_type"

class ProductOfferHandler(OfferHandler):
    
    def __init__(self) -> None:
        super.__init__()
        self.offers :Dict[int,List[ProductOffer]]= defaultdict(list)
    
    def add_new_offer(self,query):
        query_props = query.split("|")
        offer_name  = query_props[0]
        offer_id,prod_id,quantity,discount = int(query_props[1]),int(query_props[2]),int(query_props[3]),int(query_props[4])/100
        new_offer = ProductOffer(offer_id,offer_name,discount,prod_id,quantity)
        
        self.offers[prod_id].append(new_offer)
        print("Added Product Offer")
    
    def apply_offer(self,order:Order):
        
        for entry in order.cart:
        
            #need to check already offer is applied or not
            if entry.offer_id == None and self.__does_have_offer(entry.product.id):
                
                best_offer = self.__get_best_offer_for_prod(entry.product.id,entry.requested_quantity)
                
                entry.offer_id = best_offer.id
                entry.net_price = int(entry.actual_price - (entry.actual_price*best_offer.discount))
        
        return Order

    def __get_best_offer_for_prod(self,prod_id,requested_quantity):

        best_offer:ProductOffer = None
        offers = self.offers[prod_id]

        for offer in offers:
            if requested_quantity >= offer.min_quantity and ( best_offer is None or best_offer.discount < offer.discount):
                best_offer = offer
        
        return best_offer
    
        
    def __does_have_offer(self,prod_id):
        return self.offers.get(prod_id) is not None

    