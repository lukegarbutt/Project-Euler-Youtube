# 1000-digit Fibonacci numbers
def main():
	index = 2
	fib_list = [1,1]
	while(len(str(fib_list[-1])) < 1000):
		fib_list.append(fib_list[-1] + fib_list[-2])
		index += 1
	print(index)

main()