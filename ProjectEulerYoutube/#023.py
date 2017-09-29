# Non-abundant sums
import time
def main():
	dict_of_numbers = {}
	list_of_abundant_numbers = []
	for i in range(1, 28124):
		dict_of_numbers[i] = i
	for i in dict_of_numbers:
		if i < sum(factorise(i)):
			list_of_abundant_numbers.append(i)

	print('factoring done')

	for number_1 in list_of_abundant_numbers:
		for number_2 in list_of_abundant_numbers:
			total = number_1 + number_2
			if total in dict_of_numbers:
				dict_of_numbers.pop(total)
	print(dict_of_numbers)
	print(sum(dict_of_numbers))

def factorise(number):
	factors = []
	x = 1
	while(x < number):
		if number % x == 0:
			factors.append(x)
		x += 1
	return(factors)

start_time = time.time()
main()
print(time.time()-start_time)