# Goldbach's other conjecture
import time


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


def main():
    prime_list = [2,3,5,7,11]
    odd_number = 3
    while True:
        while odd_number > prime_list[-1]:
            prime_list = find_next_prime(prime_list)
        if odd_number not in prime_list:
            # then we have an odd composite
            i = 1
            success = False
            while ((2 * i**2) < odd_number) and not success:
                for prime in prime_list:
                    if prime + (2*(i**2)) == odd_number:
                        print("found one where it works", odd_number, prime, i)
                        success = True
                        break
                i += 1
            if not success:
                print("Found one where it doesn't work", odd_number)
                time.sleep(5)
        odd_number += 2


main()
    