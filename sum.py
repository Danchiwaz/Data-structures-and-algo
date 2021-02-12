def sumOfDigits(n):
	assert n>=0 and int(n) == n,"The number must be an integer" #unintensional case
	if n == 0:    #Base condition
		return 0
	else:
		return int(n % 10) + sumOfDigits(int(n / 10)) #Recursive case

print(sumOfDigits(104))