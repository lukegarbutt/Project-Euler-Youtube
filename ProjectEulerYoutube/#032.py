# Pandigital products
import math
import time
def find_factor_pairs(n):
	list_of_factors = []
	for divisor in range(2, math.floor(n**0.5)+1):
		if n%divisor == 0:
			list_of_factors.append(divisor)
	list_of_factor_pairs = []
	for factor in list_of_factors:
		list_of_factor_pairs.append([factor, int(n/factor)])
	return(list_of_factor_pairs)

def main():
	start_time = time.time()
	limit = 8_000
	total = 0
	for number in range(1,limit):
		if number % 100000 == 0:
			print(time.time()-start_time)
		#print('number:#', number)
		# find factors and return the pairs
		list_of_factor_pairs = find_factor_pairs(number)
		# check if a given pair and the number are pandigital
		for pair in list_of_factor_pairs:
			#print(pair)
			if pandigital_check(number, pair):
				total += number
				print(number)
				break
	print(total)

def pandigital_check(number, pair):
	string_digits = str(number)
	for factor in pair:
		string_digits += str(factor)
	if len(string_digits) != 9:
		return(False)
	digits = ['1','2','3','4','5','6','7','8','9']
	for digit in digits:
		if digit not in string_digits:
			return(False)
	return(True)

main()

#print(find_factor_pairs(4))
