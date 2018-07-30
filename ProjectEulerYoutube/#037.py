# Truncatable primes


def check_if_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def check_if_truncatable(n):
    str_n = str(n)
    if not check_if_prime(int(str_n)):
        return False
    for i in range(1,len(str_n)):
        if not check_if_prime(int(str_n[i:])):
            return False
        if not check_if_prime(int(str_n[:-(i)])):
            return False
    return True


def main():
    list_of_truncatable_primes = []
    total = 0
    i = 10
    while len(list_of_truncatable_primes) < 11:
        if check_if_truncatable(i):
            list_of_truncatable_primes.append(i)
            total += i
        i += 1
    print(list_of_truncatable_primes)
    print(total)


main()
