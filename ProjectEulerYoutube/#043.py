# sub-string divisibility
import itertools


def main():
    total = 0
    numbers_to_use = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    possibilities = list(itertools.permutations(numbers_to_use, 10))
    for possible in possibilities:
        number = int(''.join(str(i) for i in possible))
        if sub_string_check(number):
            total += number
    print(total)


def sub_string_check(number):
    primes = [2, 3, 5, 7, 11, 13, 17]
    str_number = str(number)
    for i in range(len(primes)):
        if int(str_number[i+1:i+4]) % primes[i] != 0:
            return False
    return True


main()
