def minimumWaitingTime(queries):
    queries.sort()

    totalWaitingTime=0
    for idx,duration in enumerate(queries):
        lefts = len(queries)-(idx+1)
        totalWaitingTime += duration*lefts
    return totalWaitingTime

array = [3, 2, 1, 2, 6]
print(minimumWaitingTime(array))