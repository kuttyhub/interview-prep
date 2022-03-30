from typing import List
from models.offer import Offer
from classes.order import Order

class OfferHandler:
    def __init__(self) -> None:
        self.offers:List[Offer] = []

    def add_offer(self,query):
        raise NotImplementedError

    def apply_offer(self,Order:Order):
        raise NotImplementedError
