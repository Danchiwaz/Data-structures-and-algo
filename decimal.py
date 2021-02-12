def deciamlToBinary(n):
	assert int(n) ==n ,"The number must be an integer"
	if n == 0:
		return 0
	else:
		return n%2 + 10 * deciamlToBinary(int(n/2))

print(deciamlToBinary(10453))	