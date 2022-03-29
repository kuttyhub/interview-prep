from models.offer import Offer

class ProductOffer(Offer):
    def __init__(self, id, name, discount,prod_id,min_quantity) -> None:
        super().__init__(id, name, discount)
        self.prod_id = prod_id
        self.min_quantity = min_quantity