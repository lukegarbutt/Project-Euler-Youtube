# Lattice Paths
import time

start_time = time.time()
memo = {}


def main(x, y):
    if (x, y) in memo:
        return memo[(x, y)]
    else:
        if x == 1:
            return 1
        elif y == 1:
            return 1
        else:
            val = main(x - 1, y) + main(x, y - 1)
            memo[(x, y)] = val
            return val


n = 500
print(main(n, n))
print(time.time() - start_time)

# print((14*(4**6))/3600)
