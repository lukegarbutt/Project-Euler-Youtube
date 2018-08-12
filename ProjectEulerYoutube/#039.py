# Integer Right Triangles

def find_solutions(p):
    solutions = []
    for a in range(1, p):
        for b in range(a, p-a):
            c = p - (a + b)
            if a**2 + b**2 == c**2:
                solutions.append([a,b,c])
    return solutions


def main():
    max_p = 0
    max_solutions = 0
    for p in range(1000):
        number_of_solutions = find_solutions(p)
        if len(number_of_solutions) > max_solutions:
            max_solutions = len(number_of_solutions)
            max_p = p
    print(max_p, max_solutions)


main()
