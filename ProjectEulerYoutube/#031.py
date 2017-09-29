# Coin sums
import time
def main():
	start_time = time.time()
	number_of_ways = 0
	range_size = 500
	for a in range(range_size):
		print(time.time()-start_time)
		if a*1 > 200:
			break
		for b in range(range_size):
			if a*1+b*2 > 200:
				break
			for c in range(range_size):
				if a*1+b*2+c*5 > 200:
					break
				for d in range(range_size):
					if a*1+b*2+c*5+d*10 > 200:
						break
					for e in range(range_size):
						if a*1+b*2+c*5+d*10+e*20 > 200:
							break
						for f in range(range_size):
							if a*1+b*2+c*5+d*10+e*20+f*50 > 200:
								break
							for g in range(range_size):
								if a*1+b*2+c*5+d*10+e*20+f*50+g*100 > 200:
									break
								for h in range(range_size):
									if a*1+b*2+c*5+d*10+e*20+f*50+g*100+h*200 > 200:
										break
									if (a*1+b*2+c*5+d*10+e*20+f*50+g*100+h*200) == 200:
										number_of_ways += 1
	print(number_of_ways)

main()