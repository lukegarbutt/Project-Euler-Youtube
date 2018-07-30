# Digit cancelling fractions


def cancel_digits(numerator, denominator):
    list_num = list(str(numerator))
    list_den = list(str(denominator))
    for digit in list_num:
        if digit in list_den and digit != '0':
            list_den.remove(digit)
            list_num.remove(digit)
    numerator = int(''.join(list_num))
    denominator = int(''.join(list_den))
    return numerator, denominator


def main():
    total = 1
    for i in range(10,100):
        for j in range(10,100):
            top, bottom = cancel_digits(i, j)
            try:
                if i != top or j != bottom:
                    if i != j:
                        if i/j == top/bottom:
                            if i/j < 1:
                                total *= i/j
            except:
                pass
    print(total)


main()
