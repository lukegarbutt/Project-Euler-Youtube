# Pentagon Numbers
from math import sqrt 

def is_pentagonal(n):
    k = (sqrt(24*n+1)+1)/6
    return k.is_integer()


def generate_pentagonal_number(n):
    return n*((3*n)-1)/2


def main():
    i = 2
    pent_numbers = [generate_pentagonal_number(1)]
    min_gap = 100000000
    while True:
        #print(i)
        pent_number = generate_pentagonal_number(i)
        for number in pent_numbers:
            if is_pentagonal(pent_number - number):
                #print('found -')
                if is_pentagonal(pent_number + number):
                    print('found +', pent_number, number)
                    min_gap = min(min_gap, abs(pent_number-number))
        if pent_number - pent_numbers[-1] > min_gap:
            break
        pent_numbers.append(pent_number)
        i += 1
    print(min_gap)
        
main()
