def isIsogram(a):
	charMap = {}
	for k in a:
		if k in charMap:
			return False
		else:
			charMap[k] = 1
	return True
a = raw_input().rstrip()
print("Yes" if isIsogram(a) else "No")
