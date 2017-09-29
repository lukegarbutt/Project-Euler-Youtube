# Amicable numbers

def find_divisors(n):
	potential_divisor = 1
	list_of_divisors = []
	while potential_divisor < n:
		if n % potential_divisor == 0:
			list_of_divisors.append(potential_divisor)
		potential_divisor += 1
	return(list_of_divisors)

def main():
	cap = 10_000
	number = 1
	list_of_amicable_numbers = []
	while number < cap:
		# find divisors of number
		list_of_divisors_of_number = find_divisors(number)
		# sum them
		sum_of_divisors_of_number = sum(list_of_divisors_of_number)
		# find divisors of this new number
		list_of_divisors_of_new_number = find_divisors(sum_of_divisors_of_number)
		# sum them
		sum_of_divisors_of_new_number = sum(list_of_divisors_of_new_number)
		# if this sum is equal to our original number, then we have an amicable pair, so add to our list
		if sum_of_divisors_of_new_number == number and sum_of_divisors_of_number < cap and number < cap and number < sum_of_divisors_of_number:
			list_of_amicable_numbers.append(number)
			list_of_amicable_numbers.append(sum_of_divisors_of_number)
		number += 1
	print(sum(list_of_amicable_numbers))

main()