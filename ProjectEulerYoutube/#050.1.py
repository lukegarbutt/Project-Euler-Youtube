# Consecutive prime sum

import time

def seive(n):
    prime_seive = [True] * n
    prime_seive[0] = prime_seive[1] = False
    for i, isprime in enumerate(prime_seive):
        if isprime:
            yield i
            for j in range(i*i, n, i):
                prime_seive[j] = False

def get_primes(n):
    primes = []
    for prime in seive(n):
        primes.append(prime)
    return primes

def main():
    n = 1_000_000
    primes = get_primes(n)
    longest_so_far = 0

    for i, prime in enumerate(primes[:-1]):
        counter = longest_so_far
        total = sum(primes[i:i+counter+1])

        while total < n:
            total = sum(primes[i:i+counter+1])

            if total in primes:
                prime_answer = total
                longest_so_far = counter + 1
                root = prime

            counter += 1

    print(longest_so_far, prime_answer, root)

if __name__ == "__main__":
    start = time.time()
    main()
    print(time.time() - start)
