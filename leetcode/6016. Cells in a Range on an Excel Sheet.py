def cellsInRange(s: str):
    start,last = s.split(":")
    firstLetter = start[0]
    firstRow = int(start[1])
    lastLetter = last[0]
    lastRow = int(last[1])
    result = []
    for i in range(ord(firstLetter),ord(lastLetter)+1):
        for j in range(firstRow,lastRow+1):
            temp=chr(i)+str(j)
            result.append(temp)
    print(result)
    # print(firstLetter,firstRow,lastLetter,lastRow)
s= "A1:F1"
cellsInRange(s)