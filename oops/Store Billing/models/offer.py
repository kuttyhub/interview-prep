
class Offer:
    #base class
    def __init__(self,id,name,discount) -> None:
        self.id = id
        self.name= name
        self.discount= discount
    
    def __str__(self) -> str:
        return f"{self.id} - {self.name} - {self.discount}"
