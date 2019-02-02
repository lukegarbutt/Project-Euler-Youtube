# Goldbach's other conjecture
import math

def is_composite(n):
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0:
            return True
    return False


def prime_sieve(max_prime):
    sieve = [True for i in range(max_prime)]
    ints = [i for i in range(max_prime)]
    print(ints, sieve)
    primes = []
    for i in range(2, max_prime-2):
        if sieve[i]:
            number = ints[i]
            for _ in range(2*number,max_prime,number):
                sieve[_] = False
    print(sieve)
    return(sieve)
prime_sieve(10)


def main():
    i = 1
    while True:
        if is_composite(i):
            pass