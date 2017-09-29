#Largest prime factor
import time
def main():
	start_time = time.time()
	target = 600851475143
	potential_factor = 2
	list_of_prime_factors = []

	while(target>1):
		if target % potential_factor == 0:
			list_of_prime_factors.append(potential_factor) 
			target = target/potential_factor
		else:
			potential_factor += 1
	print(list_of_prime_factors)

	print('This took {} seconds'.format(time.time()-start_time))

	
		

main()