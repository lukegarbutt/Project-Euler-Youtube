# Champernowne's Constant

def generate_constant(n):
    champ_const = '01'
    x = 2
    while len(champ_const) <= n:
        champ_const += str(x)
        x += 1
    return champ_const


def main():
    champ_constant = generate_constant(1000000)
    print(champ_constant)
    print(int(champ_constant[1]) * int(champ_constant[10]) * int(champ_constant[100]) * int(champ_constant[1000]) * int(champ_constant[10000]) * int(champ_constant[100000]) * int(champ_constant[1000000]))


main()
