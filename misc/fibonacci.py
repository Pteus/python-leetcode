def fibonacci_iterative(n):
    # if n <= 0:
    #     return []

    fib_sequence = [0, 1]
    for _ in range(2, n + 1):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[n]


# def fibonacci_recursive(n):
#     # if n <= 0:
#     #     return []
#     if n == 1:
#         return [0]
#     elif n == 2:
#         return [0, 1]
#     else:
#         fib_sequence = fibonacci_recursive(n - 1)
#         fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
#         return fib_sequence


def fibonacci_recursive_2(n):
    if n in {1, 0}:
        return n
    else:
        return fibonacci_recursive_2(n - 1) + fibonacci_recursive_2(n - 2)


def dp(n):
    if n < 2:
        return n

    dp = [0, 1]
    i = 2
    while i <= n:
        dp[0], dp[1] = dp[1], dp[0] + dp[1]
        i += 1
    return dp[1]


n = 14
print("Iterative - Fibonacci at index", n, "=", fibonacci_iterative(n))
print(
    "Iterative - Fibonacci for the first",
    n,
    "values:",
    [fibonacci_iterative(n) for n in range(14)],
)
print("Recursive - Fibonacci at index", n, "=", fibonacci_recursive_2(14))
print(
    "Recursive - Fibonacci for the first",
    n,
    "values:",
    [fibonacci_recursive_2(n) for n in range(14)],
)

print(dp(14))
