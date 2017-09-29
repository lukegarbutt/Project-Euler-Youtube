#Multiples of 3 and 5
def main():
	total = 0
	number_to_sum_to = 1000
	for i in range(number_to_sum_to):
		if i % 3 == 0 or i % 5 == 0:
			total += i

	print(total)







main()