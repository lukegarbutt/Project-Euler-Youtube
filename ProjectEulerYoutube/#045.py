# triangular, pentagonal and hexagonal


def generate_triangle_number(n):
    return(n*(n+1)/2)


def generate_pentagonal_number(n):
    return n*((3*n)-1)/2


def generate_hexagonal_number(n):
    return n*(2*n-1)


def main():
    triangle_numbers = [1]
    pentagonal_numbers = [1]
    triangle_n = 2
    pentagonal_n = 2
    hexagonal_n = 2
    while True:
        hexagonal_number = generate_hexagonal_number(hexagonal_n)
        hexagonal_n += 1
        while hexagonal_number > triangle_numbers[-1]:
            triangle_numbers.append(generate_triangle_number(triangle_n))
            triangle_n += 1
        while hexagonal_number > pentagonal_numbers[-1]:
            pentagonal_numbers.append(generate_pentagonal_number(pentagonal_n))
            pentagonal_n += 1
        if hexagonal_number in triangle_numbers and hexagonal_number in pentagonal_numbers:
            print(hexagonal_number)


main()

