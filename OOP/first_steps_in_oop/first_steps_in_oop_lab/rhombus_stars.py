def first_side():
    result = []
    for i in range(1, n + 1):
        result.append(" " * (n - i))
        result.append(f'{i * "* "}\n')

    return "".join(result)[:-1]


def second_side():
    result = []
    for i in range(n -1, 0, -1):
        result.append(" " * (n - i))
        result.append(f'{i * "* "}\n')

    return "".join(result)[:-1]


n = int(input())

print(first_side())
print(second_side())