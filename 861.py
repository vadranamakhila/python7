def isIsogram(b):
	charMap = {}
	for i in b:
		if i in charMap:
			return False
		else:
			charMap[i] = 1
	return True
b = raw_input().rstrip()
print("Yes" if isIsogram(b) else "No")
