
def factorial_recursive(num):
    if num > 1:
        return num * factorial_recursive(num -1)
    else:
        return num

print(factorial_recursive(5))