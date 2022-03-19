# implement an algorithm to determine if a string has all unique characters.
# what if you cannot use additional data structure

def isUique(string):
    #time is O(n)
    #space is o(k) k->unique characters

    hastable = {}

    for i in string:
        hastable[i] = hastable.get(i,0)+1
        if hastable[i]>1:
            return False
    return True

string = "hello"
print(isUique(string))