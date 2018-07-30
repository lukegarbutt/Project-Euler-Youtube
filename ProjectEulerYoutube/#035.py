# Circular Primes


def check_if_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True


def check_if_circular(n):
    str_n = str(n)
    for i in str_n:
        if check_if_prime(int(''.join(str_n))):
            str_n = str_n[len(str_n)-1] + str_n[:len(str_n)-1]
        else:
            return False
    return True


def main():
    list_of_circular_primes = []
    for i in range(1_000_000):
        if check_if_circular(i):
            list_of_circular_primes.append(i)
    print(len(list_of_circular_primes))

main()
