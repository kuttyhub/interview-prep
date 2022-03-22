from faulthandler import disable
from typing import List
from models.offer import Offer
from order import Order


class MultiProductOffer(Offer):
    def __init__(self, id, name, discount,products:List[int],common_quantity) -> None:
        super().__init__(id, name, discount)
        self.products=products
        self.common_quantity = common_quantity



class MultiProductHandler:
    def __init__(self) -> None:
        self.offers:List[MultiProductOffer] = []

    def add_new_offer(self,new_offer:MultiProductOffer):
        self.offers.append(new_offer)
    
    def apply_offer(self,order:Order):

        # getting list of productorders
        #seperate prod_id,quantity
        querys =set()
        for entry in order.ordered_products:
            querys.add((entry.product.id,entry.requested_quantity))
        
        best_offer = self.get_best_offer(list(querys))

        if best_offer is not  None:
            order = self.apply_offer_order(best_offer,order)
        
        return order
    
    def apply_offer_order(self,best_offer:MultiProductOffer,order:Order):

        for entry in order.ordered_products:
            if entry.product.id  in best_offer.products:
                entry.offer_id = best_offer.id
                entry.net_price = int(entry.actual_price - (entry.actual_price*best_offer.discount))
        
        return order

    def get_best_offer(self,querys):
        
        best_offer:MultiProductOffer = None
        for offer in self.offers:
            
            for (prod_id,quantity) in querys:
                if prod_id not in offer.products  or quantity < offer.common_quantity:
                    break 
            else:
                if best_offer is None or best_offer.discount < offer.discount:
                    best_offer = offer
        
        return best_offer