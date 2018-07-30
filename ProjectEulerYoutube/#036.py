# Double-base palindromes


def palindrome_check(n):
    str_n = str(n)
    for i in range(len(str_n)):
        if str_n[i] == str_n[-(i+1)]:
            continue
        else:
            return False
    return True


def convert_to_binary(n):
    if n == 0:
        return '0'
    binary = ''
    x = 1
    while x <= n:
        x *= 2
    x /= 2
    while x != 0.5:
        if x <= n:
            binary += '1'
            n -= int(x)
        else:
            binary += '0'
        x /= 2
    return binary


def main():
    total = 0
    for i in range(1_000_000):
        if palindrome_check(i):
            if palindrome_check(convert_to_binary(i)):
                total += i
    print(total)


main()
