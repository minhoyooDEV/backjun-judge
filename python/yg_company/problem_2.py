

n = 125


def func(n):
    if n < 10:
        return 0

    result = 1
    while n >= 10:
        n = n // 10
        result *= 10

    return result


print(func(125))
print(func(42))
print(func(634))
print(func(32424))
