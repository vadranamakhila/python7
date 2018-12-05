def sort(values):
	for s in range(len(values)):		
		for p in range(s, len(values)):			
			if (values[s] > values[p]):
				temp = values[s]
				values[s] = values[p]
				values[p] = temp
a = raw_input().rstrip()
aList = list(a)
sort(aList)
print("".join(aList))
