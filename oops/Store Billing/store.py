from models.inventory import Inventory
from models.product import Product
from order import Order, OrderedProduct
from offers.offer_handler import OffersHandler
from offers.product_offer import ProductOffer
from offers.multi_product_offer import MultiProductOffer

class Store:
    
    def __init__(self) -> None:
        self.inventory = Inventory()
        # self.offers=Offers()
        self.offers_handler = OffersHandler()
        self.order = Order()
    
    def add_product_to_inventory(self,properties):
        properties= properties.split("|")
        prod_id,prod_name = int(properties[0]),properties[1]
        quantity,price = map(int,properties[2:])

        new_product  = Product(prod_id,prod_name,quantity,price)
        self.inventory.add_product(new_product)
        print("Inventory updated.")

    def add_product_offer(self,properties):
        properties = properties.split("|")
        offer_name = properties[0]
        offer_id ,products,min_quantity,discount= int(properties[1]),properties[2],int(properties[3]),int(properties[4])/100

        #split products
        products = list(map(int,products.split(",")))

        if len(products) >1:#multi product offer
            new_offer = MultiProductOffer(offer_id,offer_name,discount,products,common_quantity= min_quantity)
            self.offers_handler.add_new_multi_product_offer(new_offer)
        else:
            new_offer = ProductOffer(offer_id,offer_name,discount,products[0],min_quantity)
            self.offers_handler.add_new_product_offer(new_offer)

        print("Offer Added.")
    
    def display_product_stock(self,properties):
        prod_id = int(properties)
        
        requested_product = self.inventory.get_product(prod_id)
            
        if requested_product is not None:
             print(requested_product.get_stock())
        else:
            raise Exception("Error: Product doesn't have in invetor ")

        
    
    def create_order(self,properties):
        properties = properties.split(";")

        for order_detial in properties:
            prod_id,quantity = map(int,order_detial.split("|"))
            
            requested_product = self.inventory.get_product(prod_id)
            new_prod_order = OrderedProduct(requested_product,quantity)

            self.order.add_product(new_prod_order)
        
        #apply best offer
        self.offers_handler.apply_all_offers(self.order)
        
        self.show_bill()
        self.reset_orders()
        
    
    def show_bill(self):
        print("== Bill ==")
        for order in self.order.ordered_products:
            print(order)
        print("== Total ==")
        print(self.order.get_total())
        print("========")
    
    def reset_orders(self):
        self.order.ordered_products[:] = []


if __name__ == "__main__":
    
    store = Store()

    print("Store Managing Application")
    user_manual ='''\
    Commands :
        1. INVENTORY - to add product to store
                - "INVENTORY=>ProductId|ProductName|Quantity|Price-Per-Quantity"
        
        2. STOCK - to check a product quantity in store
                - "STOCK=>Product ID"
        
        3. SALE - to sale the product
                - "SALE=>ProductId|Quantity;ProductId|Quantity"

        4. NEW-OFFER - to add offer to a specific product
                - "NEW-OFFER=>OFFER-NAME|OFFER-ID|Product-ID,Product-ID..|Minimum-Quantity|Discount-Percentage"

        5. EXIT - to exit from the application 
    '''

    print(user_manual)

    cmd = input()
    comands = cmd.split("=>")
    
    while (comands[0] != "EXIT"):
        try:
            
            match comands[0]:
                case "INVENTORY": store.add_product_to_inventory(comands[1])

                case "STOCK": store.display_product_stock(comands[1])
                
                case "NEW-OFFER": store.add_product_offer(comands[1])
                
                case "SALE": store.create_order(comands[1])

        except Exception as e:
            print(e)

        cmd = input()
        comands=cmd.split("=>")
    
    print("Sign Off...")