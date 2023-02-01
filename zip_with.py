def zip_with(fn, a1, a2):
    new_a = []
    index = 0
    len_a = get_minimum_length(a1, a2)

    while index < len_a:
        result = fn(a1[index], a2[index])

        new_a.append(result)
        index += 1

    return new_a


def zip_with2(fn, a1, a2):
    return list(map(fn, a1, a2))


def zip_with3(fn,a1,a2):
    return [fn(i,j) for i,j in zip(a1,a2)]


zip_with4=lambda fn,a1,a2: [fn(a,b) for a,b in zip(a1,a2)]


def get_minimum_length(a1, a2):
    len_a1 = len(a1)
    len_a2 = len(a2)

    return len_a1 if len_a1 <= len_a2 else len_a2


add = lambda a, b: a + b
pow = lambda a, b: a ^ b
sub = lambda a, b: a - b
max = lambda a, b: max(a, b)


def mul(value, m):
    result = ""
    index = 1
    while index <= m:
        result += value
        index += 1
    return result
