def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()
    result = Diff(redShirtHeights,blueShirtHeights)
    print(result)
    isPositiveCheck = result[0]>0
    if isPositiveCheck: 
        for i in result:
            if i<=0:
                return False
    else:
        for i in result:
            if i>=0:
                return False
    return True

def Diff(li1, li2):
    return [ value1-value2 for index, (value1, value2) in enumerate(zip(li1, li2))]
    
redShirts = [2, 4, 7, 5, 1]
blueShirts = [3, 5, 6, 8, 2]

print(classPhotos(redShirts,blueShirts))
