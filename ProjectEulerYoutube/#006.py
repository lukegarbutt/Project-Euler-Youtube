#Sum square difference
def main():
	sum_of_squares = 0
	square_of_sum = 0
	sum_of_numbers = 0
	target = 100
	for i in range(target+1):
		sum_of_squares += i**2
		sum_of_numbers += i
	square_of_sum += sum_of_numbers**2
	difference = square_of_sum - sum_of_squares
	print(difference)
main()