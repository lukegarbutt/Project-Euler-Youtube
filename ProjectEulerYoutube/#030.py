# Digit fifth powers
def main():
	cap = 360_000
	list_of_valid_numbers = []
	for number in range(cap):
		str_number = str(number)
		total = 0
		for digit in str_number:
			total += int(digit)**5
		if total == number:
			list_of_valid_numbers.append(number)
	print(list_of_valid_numbers)
	print(sum(list_of_valid_numbers))

main()