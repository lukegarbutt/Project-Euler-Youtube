# Even fibonacci numbers with recursion and memoisation
import time
import sys

sys.setrecursionlimit(2000)
memo = {}

def main():
    i = 0
    total = 0
    while True:
        fib_num = fib(i)
        if fib_num > 4_000_000:
            break
        else:
            if fib_num % 2 == 0:
                total += fib_num
        i += 1
    print(total)

def fib(n):
    if n in memo.keys():
        return(memo[n])
    if n == 0:
        return(0)
    elif n == 1:
        return(1)
    else:
        next_fib = fib(n-1) + fib(n-2)
        memo[n] = next_fib
        return next_fib

start_time = time.time()
print(fib(1500))
print('Time taken was {}'.format(time.time()-start_time))