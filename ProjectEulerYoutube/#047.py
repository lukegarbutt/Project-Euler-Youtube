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
    while(n**0.5>prime_list[-1]):
        prime_list = find_next_prime(prime_list)
    prime_factors = []
    while(n > 1):
        for prime in prime_list:
            while(n % prime == 0):
                prime_factors.append(prime)
                n /= prime
    return(prime_factors)


print(find_prime_factorisation(876878766))



