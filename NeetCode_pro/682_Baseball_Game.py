from typing import List


ops = ["5", "2", "C", "D", "+"]


def calPoints(operations: List[str]) -> int:
    stack = []
    total = 0

    for op in operations:
        if op == "C":
            stack.pop()
        elif op == "D":
            stack.append(stack[-1] * 2)
        elif op == "+":
            stack.append(stack[-1] + stack[-2])
        else:
            stack.append(int(op))

    for value in stack:
        total += value

    return total


# time and space: O(n)

print(calPoints(ops))
