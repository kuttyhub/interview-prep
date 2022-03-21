from typing import Dict


class Product:
    def __init__(self,id,name,quantity,price) -> None:
        self.product_id = id 
        self.product_name= name
        self.quantity = quantity
        self.price_per_quantity= price
    
    def __str__(self) -> str:
        return "{} - {}".format(self.product_name,self.quantity)
    
class Offer:
    def __init__(self,offer_name,offer_id,prod_id,min_quantity,discount_percent) -> None:
        self.offer_name = offer_name
        self.offer_id = offer_id
        self.product_id =prod_id
        self.min_quantity = min_quantity
        self.discount_percentage = discount_percent # set  10% as 0.1 in decimal

    def __str__(self) -> str:
        return "{} - {} - {} - {} - {}".format(self.offer_name,self.offer_id,self.product_id,self.min_quantity,self.discount_percentage)

class Order:
    def __init__(self,product,quantity,offer_id,total_price) -> None:
        self.product:Product=  product
        self.quantity = quantity
        self.offer_id=  offer_id    
        self.total_price =  total_price
    
    def __str__(self) -> str:
        return "{} - {} - {} - {} - {} - {}".format(self.product.product_id,self.product.product_name,self.quantity,self.product.price_per_quantity,self.offer_id,self.total_price)

class Store:
    def __init__(self) -> None:
        #dict used to map the product or offers 
        # to their id like mongo db keys
        
        self.ordered_porducts  = []
        self.inventory_products:Dict[any,Product] = {}
        
        # a product can have different offers based on quantity 
        # or some things like that so its map as dict[string,list]
        self.store_offers={}

    
    def add_inventory(self,id,name,quantity,price):
        new_product = Product(id,name,quantity,price)
        self.inventory_products[id]= new_product
        print("Inventory updated.")
    
    def add_offer(self,offer_name,offer_id,prod_id,quantity,discount):
        new_offer = Offer(offer_name,offer_id,prod_id,quantity,discount)
        
        self.store_offers[prod_id] = self.store_offers.get(prod_id,[])+[new_offer]
        print("Offer Added.")
    
    
    def add_product_to_orders(self,prod_id,quantity_purchased):
        selected_product:Product= self.inventory_products.get(prod_id)

        if selected_product is not None:
            
            has_quantity = selected_product.quantity >= quantity_purchased
            
            if (has_quantity):
                # add order
                best_offer:Offer  = self.get_best_discount(prod_id,quantity_purchased)

                actual_price= (selected_product.price_per_quantity * quantity_purchased) 

                if(best_offer is None):
                      new_order = Order(selected_product,quantity_purchased,"N/A",actual_price)
                else:
                    #calculate net price    
                    net_price = int(actual_price -(actual_price * best_offer.discount_percentage))
                    new_order = Order(selected_product,quantity_purchased,best_offer.offer_id,net_price)

                self.ordered_porducts.append(new_order)

                #reduce product quantity
                selected_product.quantity -= quantity_purchased
                self.inventory_products[prod_id] = selected_product

            else:
                print("store doesn't have enough quantity")
        else:
            print("Provide Valid Product")
    

    

    def get_best_discount(self,prod_id,quantiy_purchased):

        if self.store_offers.get(prod_id) is None:
            return None
        else:
            offers = self.store_offers[prod_id]
            best_offer = None
            for offer in offers:
                if quantiy_purchased >= offer.min_quantity:
                    if  best_offer is None or best_offer.discount_percentage < offer.discount_percentage:
                        best_offer  = offer

            return best_offer

    def print_bills(self):
        print("== Bill ==")
        total =0
        for order in self.ordered_porducts:
            print(order)
            total += order.total_price
        print("== Total ==")
        print(total)
        print("========")

    
    def show_product_detials(self,prod_id):
        product= self.inventory_products[prod_id]
        print(product)
       

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
                - "NEW-OFFER=>BuyXMore|OFFER-ID|Product-ID|Minimum-Quantity|Discount-Percentage"

        5. EXIT - to exit from the application 
    '''
    print(user_manual)

    cmd = input()
    comands = cmd.split("=>")
    
    while (comands[0] != "EXIT"):
        
        match comands[0]:
            case "INVENTORY":
                properties = comands[1].split("|")
                store.add_inventory(id=properties[0],name=properties[1],quantity=int(properties[2]),price=int(properties[3]))

            case "STOCK":
                prod_id = comands[1]
                store.show_product_detials(prod_id)
            
            case "NEW-OFFER":
                properties = comands[1].split("|") 
                store.add_offer(offer_name=properties[0],offer_id=properties[1],prod_id=properties[2],quantity=int(properties[3]),discount=float(properties[4])/100)
            
            case "SALE":
                products= comands[1].split(";")
                for i in products:
                    i = i.split("|")
                    prod_id,quantity = i[0],int(i[1])
                    store.add_product_to_orders(prod_id=prod_id,quantity_purchased=quantity)
                store.print_bills()
                #remove all orders for the memory 
                store.ordered_porducts = []

        cmd = input()
        comands=cmd.split("=>")

    print("Sign Off...")