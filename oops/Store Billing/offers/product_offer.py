from collections import defaultdict
from typing import Dict, List
from models.offer import Offer
from order import Order 


class ProductOffer(Offer):
    def __init__(self, id, name, discount,prod_id,min_quantity) -> None:
        super().__init__(id, name, discount)
        self.prod_id = prod_id
        self.min_quantity = min_quantity

class ProductOfferHandler:
    
    def __init__(self) -> None:
        self.offers :Dict[int,List[ProductOffer]]= defaultdict(list)
    
    def add_new_offer(self,new_offer:ProductOffer):
        self.offers[new_offer.prod_id].append(new_offer)
    
    def apply_offer(self,order:Order):
        
        for entry in order.ordered_products:
            
            #need to check already offer is applied or not
            if entry.offer_id == "N/A" and self.does_have_offer(entry.product.id):
                
                best_offer = self.get_best_offer(entry.product.id,entry.requested_quantity)
                entry.offer_id = best_offer.id
                entry.net_price = int(entry.actual_price - (entry.actual_price*best_offer.discount))
        
        return Order

    def get_best_offer(self,prod_id,requested_quantity):

        best_offer:Offer = None
        offers = self.offers[prod_id]

        for offer in offers:
            if requested_quantity >= offer.min_quantity and ( best_offer is None or best_offer.discount < offer.discount):
                best_offer = offer
        
        return best_offer
    
        
    def does_have_offer(self,prod_id):
        return self.offers.get(prod_id) is not None

    