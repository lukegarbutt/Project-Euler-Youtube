#10001st prime
import time
def main():
	start_time = time.time()
	number_prime_to_find = 20001
	x = 2
	list_of_primes = []

	list_of_primes_to_check = []
	index = 0

	while(len(list_of_primes) < number_prime_to_find):
	 	if all(x % prime for prime in list_of_primes_to_check):
	 		list_of_primes.append(x)
	 		if list_of_primes[index] < x**0.5 + 1:
	 			list_of_primes_to_check.append(list_of_primes[index])
	 			index += 1
	 			#print(list_of_primes, list_of_primes_to_check, x)
	 	x += 1


	#print(list_of_primes)
	print(list_of_primes[-1])
	print(time.time()-start_time)

main()
