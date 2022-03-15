#kutty's playground

def spiralTraverse(array):
    if len(array)<=0:
        return []

    result = []
    startRow,endRow = 0,len(array)-1
    startCol,endCol = 0,len(array[0])-1
    printouterLayer(array,result,startRow,startCol,endRow,endCol)
    return result

def printouterLayer(array,result,startRow,startCol,endRow,endCol):
    if startRow >endRow or startCol>endCol:
        return

    for col in range(startCol,endCol+1):
        result.append(array[startRow][col])
    for row in range(startRow+1,endRow+1):
        result.append(array[row][endCol])
    for col in reversed(range(startCol,endCol)):
        if startRow == endRow:
            break
        result.append(array[endRow][col])
    for row in reversed(range(startRow+1,endRow)):
        if startCol == endCol:
            break
        result.append(array[row][startCol])
    printouterLayer(array,result,startRow+1,startCol+1,endRow-1,endCol-1)

arr = [
    [19, 32, 33, 34, 25, 8],
    [16, 15, 14, 13, 12, 11],
    [18, 31, 36, 35, 26, 9],
    [1, 2, 3, 4, 5, 6],
    [20, 21, 22, 23, 24, 7],
    [17, 30, 29, 28, 27, 10]
  ]
res=[]
print(spiralTraverse(arr,res))
home = [19, 32, 33, 34, 25, 8, 11, 9, 6, 7, 10, 27, 28, 29, 30, 17, 20, 1, 18, 16, 15, 14, 13, 12, 26, 5, 24, 23, 22, 21, 2, 31, 36, 35, 4, 3]