#Kutty's Playground

def hasSingleCycle(array):
    steps = 0
    idx =0
    while steps < len(array):
        #finded inner loop
        if steps>0 and idx == 0:
            return False
        steps+=1
        idx += array[idx]
        idx %= len(array)
    return idx == 0

array =[2, 3, 1, -4, -4, 2]
print(hasSingleCycle(array))