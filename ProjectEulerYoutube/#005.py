#Smallest Multiple
import time
def main():
	start_time = time.time()
	target = 20
	x = 1
	answer_found = False
	while(True):
		for i in range(1,target+1):
			if x % i != 0:
				break
			if i == target:
				answer_found = True
		if answer_found:
			break
		x += 1
	print(x)
	print('Answer is {}, this took {} seconds to find'.format(x, time.time()-start_time))

main()












































