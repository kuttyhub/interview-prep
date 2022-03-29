from typing import List
from models.offer import Offer

class MultiProductOffer(Offer):
    def __init__(self, id, name, discount,products:List[int],common_quantity) -> None:
        super().__init__(id, name, discount)
        self.products=products
        self.common_quantity = common_quantity

    def __str__(self) -> str:
        return super().__str__() + f"-{self.products}-{self.common_quantity}"