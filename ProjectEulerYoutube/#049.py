# Prime Permutations

def all_primes_under(n):
    # can make this more efficient by only checking primes under sqrt of number_to_check
    assert n > 2
    primes = [2]
    number_to_check = 3
    while number_to_check < n:
        if not any([number_to_check%x == 0 for x in primes]):
            primes.append(number_to_check)
        number_to_check += 2
    return primes

def main():
    primes = all_primes_under(10000)
    primes_over_1000 = [i for i in primes if i >= 1000]
    for prime in primes:
        for gap in range(2, 4500, 2):
            prime_2 = prime + gap
            prime_3 = prime + (2 * gap)
            if prime_2 in primes_over_1000 and prime_3 in primes_over_1000:
                if sorted(list(str(prime))) == sorted(list(str(prime_2))) == sorted(list(str(prime_3))):
                    print(str(prime) + str(prime_2) + str(prime_3))

if __name__ == '__main__':
    main()
