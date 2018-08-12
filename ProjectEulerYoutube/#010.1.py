# Summation of primes
import time

def main():
    max_prime = 10000000
    sieve = [True for i in range(max_prime)]
    sieve[0:1] = [False, False]
    x = 0
    while x <= max_prime:
        if sieve[x]:
            for j in range(2*x, max_prime+1, x):
                sieve[j] = False
        x += 1

    primes = []
    counter = 0
    for item in sieve:
        if item:
            primes.append(counter)
        counter += 1
    print(sum(primes))


start_time = time.time()
main()
print(time.time()-start_time)
