from typing import List
from classes.inventory import Inventory
from classes.order import Order, CartItem
from classes.offers.offer_handler import OffersHandler

class Store:
    
    inventory = Inventory()
    offers_handler = OffersHandler()
    orders = []
    
    def __add_product_to_inventory(self,query):
        Store.inventory.add_product(query)

    
    def __add_offer(self,query):
        Store.offers_handler.add_new_offer(query);
    
    def __display_product_stock(self,properties):
        prod_id = int(properties)
        Store.inventory.display_product_stock(prod_id)
    
    def __make_order(self,query):

        cart_entries:List[CartItem] = self.__get_entrys_from_query(query);        
        order = Order(cart_entries);

        Store.inventory.reduce_quantity(cart_entries)
        
        Store.offers_handler.apply_all_offers(order)
        
        order.show_bill()
        Store.orders.append(order);

    
    def __get_entrys_from_query(self,query)-> List[CartItem]:
        
        cart_entries = []

        query_props = query.split(";")

        for cart_item in query_props:
            prod_id,quantity = map(int,cart_item.split("|"))
            requested_product = Store.inventory.get_product(prod_id)

            # check quantity 
            if requested_product.quantity <quantity:
                raise Exception("Not enough quantity in Inventory")

            new_cart_item = CartItem(requested_product,quantity)
            cart_entries.append(new_cart_item);
        
        return cart_entries
    
    def __show_commands(self):
        user_manual ='''\
        Commands :
            1. INVENTORY - to add product to store
                    - "INVENTORY=>ProductId|ProductName|Quantity|Price-Per-Quantity"
            
            2. STOCK - to check a product quantity in store
                    - "STOCK=>Product ID"
            
            3. SALE - to sale the product
                    - "SALE=>ProductId|Quantity;ProductId|Quantity"

            4. NEW-OFFER - to add offer to a specific product
                    - "NEW-OFFER=>OFFER-NAME|OFFER-ID|Product-ID,Product-ID..|Minimum-Quantity|Discount-Percentage|offer_type"

            5. EXIT - to exit from the application 
        '''
        print(user_manual)

    def __executeComand(self,comands):
        
        comands=comands.split("=>")
        try:    
            match comands[0]:
                case "INVENTORY": self.__add_product_to_inventory(comands[1])

                case "STOCK": self.__display_product_stock(comands[1])
                
                case "NEW-OFFER": self.__add_offer(comands[1])
                
                case "SALE": self.__make_order(comands[1])
                
                case "HELP": self.__show_commands()

                case "EXIT": 
                    print("Sign off")
                    exit()

        except Exception as e:
            print(e)


    def start_day(self):
        print("Store Managing Application")
        self.__show_commands();

        while True:
            cmd = input()
            self.__executeComand(cmd)
        