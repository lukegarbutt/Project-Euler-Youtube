# triangular, pentagonal and hexagonal
import math
from math import sqrt 

def is_pentagonal(n):
    k = (sqrt(24*n+1)+1)/6
    return k.is_integer()

def generate_pentagonal_number(n):
    return n*((3*n)-1)/2

def is_triangle(n):
    root = math.sqrt(n)
    if int(root + 0.5) ** 2 == n:
        return True
    else:
        return False

def generate_hexagonal_number(n):
    return n*(2*n-1)

def main():
    i = 2
    while True:
        number = generate_hexagonal_number(i)
        if is_pentagonal(number) and is_triangle(number):
            print(number)
            break
        i += 1
        print(i)

main()

