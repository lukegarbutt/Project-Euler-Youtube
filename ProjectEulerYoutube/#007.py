#10001st prime
import time
def main():
	start_time = time.time()
	number_prime_to_find = 20001
	x = 2
	list_of_primes = []
	while(len(list_of_primes) < number_prime_to_find):
	 	if all(x % prime for prime in list_of_primes):
	 		list_of_primes.append(x)
	 	x += 1


	#print(list_of_primes)
	print(list_of_primes[-1])
	print(time.time()-start_time)

main()
