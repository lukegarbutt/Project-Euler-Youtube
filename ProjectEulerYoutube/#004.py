#Larget palindrome product
import time
def main():
	start_time = time.time()
	list_of_palindromes = []

	for x in range(100, 1000):
		for y in range(x, 1000):
			if is_palindrome(x*y):
				list_of_palindromes.append(x*y)

	print(max(list_of_palindromes))
	print('Time taken {} and our answer is {}'.format(time.time()-start_time, max(list_of_palindromes)))

	





def is_palindrome(test):
	test = str(test)
	if test == test[::-1]:
		return(True)
	else:
		return(False)



main()