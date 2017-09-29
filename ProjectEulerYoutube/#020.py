# Factorial digit sum

def factorial(n):
	if n == 0:
		return(1)
	elif n == 1:
		return(1)
	else:
		return(n*factorial(n-1))

def main():
	x = 100
	answer = factorial(x)
	digits = list(str(answer))
	#print(digits)
	sum_of_digits = 0
	for digit in digits:
		sum_of_digits += int(digit)
	print(sum_of_digits)

main()
