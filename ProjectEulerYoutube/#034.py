# Digit factorials


def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial(n-1)


def main():
    grand_total = 0
    for i in range(10, 1000000):
        str_i = str(i)
        total = 0
        for digit in str_i:
            digit = int(digit)
            total += factorial(digit)
        if total == i:
            grand_total += i
            print(i, grand_total)


main()
