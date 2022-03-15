#kutty's playground

def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    mindiff = float("inf")
    res = []
    for i in arrayOne:
        for j in arrayTwo:
            temp = abs(i-j)
            if temp == 0:
                return[i,j]
            elif temp < mindiff:
                mindiff = temp
                res =[i,j]
    return res

arrayone = [-1, 5, 10, 20, 28, 3]
arraytwo = [26, 134, 135, 15, 17]

print(smallestDifference(arrayone,arraytwo))