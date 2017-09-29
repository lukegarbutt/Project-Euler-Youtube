# Reciprocal cycles
import time

def main():
	d = 1000
	max_cycle_length = 0
	i_that_produced_cycle = False
	for i in range(1,d):
		current_cycle = find_cycle_length(i)
		if current_cycle > max_cycle_length:
			max_cycle_length = current_cycle
			i_that_produced_cycle = i
	print(i_that_produced_cycle)

def find_cycle_length(n):
	cycle_length = 0
	list_of_remainders = []
	x = 1
	while(True):
		if x % n == 0:
			break
		elif x in list_of_remainders:
			break
		list_of_remainders.append(x)
		x = (x*10) % n
		cycle_length += 1
	return(cycle_length)

start_time = time.time()
main()
print('time taken was {} seconds'.format(time.time()-start_time))
