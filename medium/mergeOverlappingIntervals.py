#kutty's playground

def mergeOverlappingIntervals(intervals):
	startPoint = float("-inf")
	endPoint = float("-inf")
	res= []

	intervals.sort()
	
	for start,end in intervals:       
		# update range
		if endPoint < start:
			res.append([startPoint,endPoint])
			startPoint = start
			endPoint = end

		if endPoint < end:
			endPoint =end
	
	res.append([startPoint,endPoint])
    
	#for remove the (-inf,-inf) element added on first try
	res.pop(0)
	return res


intervals= [
    [1, 2],
    [3, 5],
    [4, 7],
    [6, 8],
    [9, 10]
]

print(mergeOverlappingIntervals(intervals))
