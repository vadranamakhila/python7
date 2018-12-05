b = raw_input().rstrip()
evenA = oddA = ''
for i, n in enumerate(b):
	if i & 1 == 0:
		evenA += n
	else:
		oddA += n

print(evenB + " " + oddB)
