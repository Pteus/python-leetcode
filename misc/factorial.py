# 5! = 5 * 4 * 3 * 2 * 1 = 5 * (n-1) * (n-2) ... * 1


def factorial_interative(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact


def factorial_recursive(n):
    if n in {0, 1}:
        return 1
    else:
        return n * factorial_recursive(n - 1)


print(factorial_interative(5))
print(factorial_recursive(5))
