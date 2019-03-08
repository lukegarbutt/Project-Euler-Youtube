# Distinct prime factors


def find_next_prime(prime_list):
    n = prime_list[-1] + 2
    prime_found = False
    while not prime_found:
        prime_max = n**0.5
        for prime in prime_list:
            if prime > prime_max:
                prime_found = True
                prime_list.append(n)
                break
            if n % prime == 0:
                break
        n += 2
    return prime_list


def find_prime_factorisation(n, prime_list=[2,3]):
    while(n**0.5+1>prime_list[-1]):
        prime_list = find_next_prime(prime_list)
    prime_factors = []
    while(n > 1):
        _in = n
        for prime in prime_list:
            while(n % prime == 0):
                prime_factors.append(prime)
                n /= prime
        if _in == n:
            prime_factors.append(n)
            n /= n
    return(prime_factors)


def main():
    x = 1
    while True:
        passed_tests = True
        prime_factors = [find_prime_factorisation(x), find_prime_factorisation(x+1), find_prime_factorisation(x+2), find_prime_factorisation(x+3)]
        # prime_factors = [find_prime_factorisation(x), find_prime_factorisation(x+1), find_prime_factorisation(x+2)]
        for factor_list in prime_factors:
            if len(set(factor_list)) != 4:
                passed_tests = False
        if passed_tests:
            break
        x += 1
    print(x)
    print(prime_factors)


main()