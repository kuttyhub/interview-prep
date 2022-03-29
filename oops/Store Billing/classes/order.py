from typing import List
from models.cart_item import CartItem

class Order:
    
    def __init__(self,cart_entries:List[CartItem]) -> None:
        
        if len(cart_entries) == 0:
            raise Exception("Cannot create a Order without products");
        
        self.__cart:List[CartItem] = cart_entries
    

    @property #make ready only property for cart 
    def cart(self):
        return self.__cart;

    def __get_total(self) -> int:
        total = 0
        for cart_item  in self.__cart:
            total += cart_item.net_price
        return total
    
    def show_bill(self):
        print("== Bill  ==")

        for car_item in self.__cart:
            print(car_item)

        print("== Total ==")
        print(self.__get_total())
        print("===========")

    