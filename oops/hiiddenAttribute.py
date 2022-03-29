class Hello:
    __hidden = 10

    def __init__(self) -> None:
        print("from init method -> ",self.__hidden)

obj = Hello()
try:
    print(obj.__hidden)
# except AttributeError:
except Exception as err:
    # print("'Hello' object has no attribute '__hidden'")
    print(err)

#accessing hidden attribute via class name forward bt an udderscore
print(obj._Hello__hidden)