def do_stuff(input):p
	, op, q = [p for p in input.split(" ")]
	if op == '/':
		print(int(p) / int(q))
	else:
		print(int(p) % int(q))
while True:
  try:
    value = raw_input()
    do_stuff(value.rstrip()) # next line was found 
  except (EOFError):
    break #end of file reached
