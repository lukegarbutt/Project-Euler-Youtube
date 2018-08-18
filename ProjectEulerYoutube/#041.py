# Pandigital prime

def prime_check(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    biggest_so_far = 0
    numbers_to_use = []
    for digit in range(1,10):
        numbers_to_use.append(digit)


