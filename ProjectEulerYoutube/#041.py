# Pandigital prime
import itertools

def prime_check(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    biggest_so_far = 0
    for length_of_number in range(9, 1, -1):
        numbers_to_use = []
        for digit in range(length_of_number, 0, -1):
            numbers_to_use.append(digit)
        possibilities = list(itertools.permutations(numbers_to_use, length_of_number))
        for possible in possibilities:
            number = int(''.join(str(i) for i in possible))
            if prime_check(number):
                print(number)
                quit()


main()
