#kutty's playground 

def firstDuplicateValue(array):
    seen = set()
    for i in array:
        if i in seen:
            return i
        else:
            seen.add(i)

    return -1

array = [2,1,5,2,3,3,4]

print(firstDuplicateValue(array))