# Quadratic primes
def main():
	max_number_of_primes = 0
	a_b_to_make_primes = False
	for a in range(-999, 1000, 2):
		#print(a)
		for b in range(2, 1000):
			if not prime_check(b):
				continue
			n = 0
			current_number_of_primes = 0
			while(True):
				if (n**2 + a*n + b) < 0:
					break
				if prime_check(n**2 + a*n + b):
					current_number_of_primes += 1
				else:
					if current_number_of_primes > max_number_of_primes:
						max_number_of_primes = current_number_of_primes
						a_b_to_make_primes = a*b
					break
				n += 1
	print(a_b_to_make_primes)

def prime_check(n):
	if n % 2 == 0:
		return(False)
	for i in range(3,n,2):
		if n % i == 0:
			return(False)
	return(True)

main()