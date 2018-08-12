# Pandigital multiples

def check_if_pandigital(n):
    str_n = str(n)
    if len(str_n) != 9:
        return False
    for i in range(1,10):
        if str(i) not in str_n:
            return False
    return True

def concatonate_products(n):
    x = 2
    result = str(n)
    while len(result) < 9:
        result += str(n*x)
        x += 1
    return result

def main():
    answers = []
    for i in range(100_000):
        concat = concatonate_products(i)
        if check_if_pandigital(concat):
            print(i, concat)
            answers.append(concat)
    print(max(answers))

main()
