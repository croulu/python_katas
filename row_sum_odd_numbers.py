def row_sum_odd_numbers(n):
    return sum_elements(create_odds_for_me(n))


def say_odd(n):
    return n % 2 != 0


def create_odds_for_me(n):
    odds = []
    index_triangle = 1
    index_numbers = 1

    while index_triangle <= n:
        while len(odds) < index_triangle:
            if say_odd(index_numbers):
                odds.append(index_numbers)
            index_numbers += 1
        if index_triangle != n:
            odds = []
        index_triangle += 1

    return odds


def sum_elements(numbers):
    index = 0
    sum = 0

    while index < len(numbers):
        sum += numbers[index]
        index += 1

    return sum
