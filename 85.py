a = raw_input().rstrip()
evenA = oddA = ''
for j, k in enumerate(a):
	if j & 1 == 0:
		evenA += k
	else:
		oddA += k

print(evenA + " " + oddA)
