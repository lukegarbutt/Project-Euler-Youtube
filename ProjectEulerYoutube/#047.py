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


def group_factorisation(factors):
    factors_dict = {}
    for factor in factors:
        if factor in factors_dict.keys():
            factors_dict[factor] += 1
        else:
            factors_dict[factor] = 1
    return(factors_dict)


def main():
    x = 1
    while True:
        prime_factors_1 = group_factorisation(find_prime_factorisation(x))
        prime_factors_2 = group_factorisation(find_prime_factorisation(x+1))
        prime_factors_3 = group_factorisation(find_prime_factorisation(x+2))
        prime_factors_4 = group_factorisation(find_prime_factorisation(x+3))
        failed = False
        if not failed:
            for key, value in prime_factors_1.items():
                if key in prime_factors_2 and value == prime_factors_2[key]:
                    failed = True
                elif key in prime_factors_3 and value == prime_factors_3[key]:
                    failed = True
                elif key in prime_factors_4 and value == prime_factors_4[key]:
                    failed = True
        if not failed:
            for key, value in prime_factors_2.items():
                if key in prime_factors_3 and value == prime_factors_3[key]:
                    failed = True
                elif key in prime_factors_4 and value == prime_factors_4[key]:
                    failed = True
        if not failed:
            for key, value in prime_factors_3.items():
                if key in prime_factors_4 and value == prime_factors_4[key]:
                    failed = True
        if not failed:
            print("success, our numbers are {}, {}, {} and {}. The factors were {}, {}, {} and {}".format(x, x+1, x+2, x+3, prime_factors_1, prime_factors_2, prime_factors_3, prime_factors_4))
            break
        x += 1


main()