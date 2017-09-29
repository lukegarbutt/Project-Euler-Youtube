#Power Digit Sum
def main():
	total = 2**1000
	total = str(total)
	answer = 0
	for i in range(len(total)):
		answer += int(total[i])
	print(answer)
main()