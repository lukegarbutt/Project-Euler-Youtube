#Smallest Multiple improved
import time
def main():
	start_time = time.time()
	lcm_up_to = 1000
	list_of_list_of_prime_factors = []
	answer = 1

	for i in range(2, lcm_up_to+1):
		target = i
		potential_factor = 2
		list_of_prime_factors = []

		while(target>1):
			if target % potential_factor == 0:
				list_of_prime_factors.append(potential_factor) 
				target = target/potential_factor
			else:
				potential_factor += 1
		#print(list_of_prime_factors)
		list_of_list_of_prime_factors.append(list_of_prime_factors)

	print(list_of_list_of_prime_factors)

	#iterate over list of list
	#find each number, and how many times it appears
	#find the place it appears most
	#multiply our answer by this number this many times
	list_of_numbers_to_check = []
	for primes in list_of_list_of_prime_factors:
		for prime in primes:
			if prime not in list_of_numbers_to_check:
				list_of_numbers_to_check.append(prime)

	for prime in list_of_numbers_to_check:
		max_count = 0
		for primes in list_of_list_of_prime_factors:
			count = 0
			for i in primes:
				if prime == i:
					count += 1
			if count > max_count:
				max_count = count
		print(prime, max_count)
		answer *= prime**max_count
	print(answer)
	print(len(str(answer)))
	print('The answer is {} this is {} digits long, this took {} seconds to find'.format(answer, len(str(answer)), time.time()-start_time))


	#print(list_of_numbers_to_check)
main()