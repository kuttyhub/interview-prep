class Product:
    def __init__(self,id,name,quantity,price) -> None:
        self.id = id 
        self.name= name
        self.quantity = quantity
        self.price= price
    
    
    def has_requested_quantity(self,requested_quantity:int) -> bool:
        return requested_quantity <= self.quantity
    
    def update_quantity(self,value):
        self.quantity += value
    #updating quantity will be done here


    def __str__(self) -> str:
        return "{} - {} - {} - {}".format(self.id,self.name,self.quantity,self.price)

    def display_stock(self) -> str:
        return "{} - {}".format(self.name,self.quantity)