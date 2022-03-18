class Base1:
    def __init__(self,value) -> None:
        print("initiate base1 class")
        self.value = value

class Base2:
    def __init__(self,value) -> None:
        print("initate base2 class")
        self._value= value

class Base3:
    def __init__(self,value) -> None:
        print("initate base3 class")
        self.___value= value

class Derived(Base1,Base2,Base3):
    __private = "private"
    def __init__(self, value) -> None:
        # super().__init__(value)
        Base1.__init__(self,value)
        Base2.__init__(self,12)
        Base3.__init__(self,13)
        print(self.value)
        print(self._value)
        print(Base2.__new__)
        print(self.__private)
        

obj = Derived(10)
base2 = Base2(20)
print(base2._value)
