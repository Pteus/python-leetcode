def fizzbuzz(n):
    for i in range(1, n + 1):
        # if i % 15 == 0:
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


def fizzbuzz_2(n):
    result = ""
    for i in range(1, n + 1):
        if i % 3 == 0:
            result += "Fizz"
        if i % 5 == 0:
            result += "Buzz"
        if not (i % 3 == 0 or i % 5 == 0):
            result += str(i)
        result += "\n"  # Add a newline after each number or combination
    return result


# Example usage:
# fizzbuzz(15)
print(fizzbuzz_2(15))
