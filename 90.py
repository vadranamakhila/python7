def sort(values):
	for i in range(len(values)):		
		for q in range(i, len(values)):			
			if (values[i] > values[q]):
				temp = values[i]
				values[i] = values[q]
				values[q] = temp
b = raw_input().rstrip()
bList = list(b)
sort(bList)
print("".join(bList))
