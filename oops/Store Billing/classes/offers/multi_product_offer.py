from faulthandler import disable
from typing import List
from models.multi_product_offer import MultiProductOffer 
from classes.order import Order


# "NEW-OFFER=>OFFER-NAME|OFFER-ID|Product-ID,Product-ID..|Minimum-Quantity|Discount-Percentage|offer_type"

class MultiProductHandler:
    def __init__(self) -> None:
        self.offers:List[MultiProductOffer] = []

    def add_new_offer(self, query):
        query_props = query.split("|")
        offer_name  = query_props[0]
        offer_id= int(query_props[1])
        products= list(map(int,query_props[2].split(",")))
        quantity,discount = int(query_props[3]),int(query_props[4])/100
        
        new_offer = MultiProductOffer(offer_id,offer_name,discount,products,quantity)
        print(new_offer)
        self.offers.append(new_offer)
        print("Added Multi product Offer")
    
    
    def apply_offer(self,order:Order):

        order_ids ={}
        for cart_item in order.cart:
            order_ids[cart_item.product.id]=cart_item.requested_quantity
        
        best_offer = self.__get_best_offer(order_ids)

        if best_offer is not  None:
            order = self.__apply_offer_order(best_offer,order)
        
        return order
    
    def __apply_offer_order(self,best_offer:MultiProductOffer,order:Order):

        for cart_item in order.cart:
            if cart_item.product.id  in best_offer.products:
                cart_item.offer_id = best_offer.id
                cart_item.net_price = int(cart_item.actual_price - (cart_item.actual_price*best_offer.discount))
        return order

    def __get_best_offer(self,order_ids):
        
        best_offer:MultiProductOffer = None
        
        for offer in self.offers:
                
            is_best_offer=  self.__is_offer_applicable(offer,order_ids) and (best_offer is None or best_offer.discount < offer.discount)
            if is_best_offer:
                best_offer = offer
        
        return best_offer
    
    def __is_offer_applicable(self,offer,order_ids):
        for prod_id in offer.products:
            if prod_id in order_ids and order_ids[prod_id] < offer.common_quantity: 
                #offer not applicable
                return False
        return True