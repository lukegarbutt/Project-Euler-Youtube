#Lattice Paths
import time
start_time = time.time()
def main(x, y):
	if x == 1:
		return(1)
	elif y == 1:
		return(1)
	else:
		return(main(x-1,y) + main(x,y-1))


n=15
print(main(n,n))
print(time.time()-start_time)

#print((14*(4**6))/3600)



