# coin sums

def find_number_of_ways(current_total, total, possible_coins, number_of_ways):
    for index in range(len(possible_coins)):
        new_total = current_total + possible_coins[index]
        if new_total == total:
            number_of_ways += 1
        elif new_total > total:
            return number_of_ways
        else:
            number_of_ways = find_number_of_ways(new_total, total, possible_coins[index:], number_of_ways)
    return number_of_ways


def main():
    total = 200
    possible_coins = [1, 2, 5, 10, 20, 50, 100, 200]
    current_total = 0
    number_of_ways = 0
    print(find_number_of_ways(current_total, total, possible_coins, number_of_ways))

main()