class Test:
    firstName = "Kutty"
    lastName = "Nishanth"
    def __init__(self) -> None:
        print("Class initiated")
    
    def __str__(self) -> str:
        return "This is test Class with value -> " + self.firstName+self.lastName

    def __repr__(self) -> str:
        return "This is test Reprentation [{}] [{}]".format(self.firstName,self.lastName)

obj = Test()
print(obj) #call's __str__
print([obj]) #call's __repr__