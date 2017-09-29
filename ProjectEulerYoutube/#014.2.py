#Longest Collatz Sequence
import time
def main():
	start_time = time.time()
	current_longest_chain = 0
	number_that_produced_chain = 0
	x = 1
	number_to_collatz_up_to = 10_000_000
	dict_of_known_collatz = {1:1}

	while(x < number_to_collatz_up_to):
		numbers_in_chain = []
		current_number = x
		current_chain = 1
		while(current_number != 1):
			if current_number in dict_of_known_collatz.keys():
				current_chain += dict_of_known_collatz[current_number]-1
				break
			numbers_in_chain.append(current_number)
			current_number = collatz(current_number)
			current_chain += 1
		if current_chain > current_longest_chain:
			current_longest_chain = current_chain
			number_that_produced_chain = x
		for i in numbers_in_chain:
			dict_of_known_collatz[i] = current_chain
			#print('The length of the chain for {} is {}'.format(i, current_chain))
			current_chain -= 1
		#print(dict_of_known_collatz)
		current_chain = 1
		x += 1
	print('The longest chain was {}, the number that produced this chain was {}, this took {} seconds to find'.format(current_longest_chain, number_that_produced_chain, time.time()-start_time))



def collatz(number):
	if number % 2 == 0:
		number = number/2
	else:
		number = (number * 3) + 1
	number = int(number)
	return(number)
main()


