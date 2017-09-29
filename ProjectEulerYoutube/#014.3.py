#Longest Collatz Sequence
from functools import lru_cache
import time

def main():
	start_time = time.time()
	for x in range(1, 1_000_000):
		length = 0
		while x != 1:
			x = collatz(x)
			length += 1
	print(time.time()-start_time)

	
@lru_cache(maxsize = 2048)
def collatz(number):
	if number % 2 == 0:
		number = number/2
	else:
		number = (number * 3) + 1
	return(number)
main()


