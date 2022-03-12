def findThreeLargestNumbers(array):
	first=second=third =float("-inf")
	for i in array:
		if i >first:
			third = second
			second = first
			first = i
		elif i> second:
			third = second
			second = i
		elif i>third:
			third = i
	return [third,second,first]
			
a = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
print(findThreeLargestNumbers(a))