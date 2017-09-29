# Distinct powers
import time
def main():
	list_of_numbers = []
	for a in range(2,101):
		for b in range(2,101):
			number = a**b
			if number not in list_of_numbers:
				list_of_numbers.append(number)
	list_of_numbers.sort()
	print(len(list_of_numbers))
start_time = time.time()
main()
print('Time taken was {} seconds'.format(time.time()-start_time))