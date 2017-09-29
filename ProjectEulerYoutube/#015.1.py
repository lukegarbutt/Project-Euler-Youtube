#Lattice Paths
import time
from functools import lru_cache
start_time = time.time()
@lru_cache(maxsize=128)
def main(x, y):
	if x == 1:
		return(1)
	elif y == 1:
		return(1)
	else:
		return(main(x-1,y) + main(x,y-1))


n=20
print(main(n,n))
print(time.time()-start_time)
print(main.cache_info())

#print((14*(4**6))/3600)

