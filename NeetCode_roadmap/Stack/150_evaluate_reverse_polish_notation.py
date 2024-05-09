from typing import List


tokens = ["2", "1", "+", "3", "*"]


def evalRPN(tokens: List[str]) -> int:
    stack = []

    for token in tokens:
        if token == "+":
            stack.append(stack.pop() + stack.pop())
        elif token == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif token == "*":
            stack.append(stack.pop() * stack.pop())
        elif token == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))
        else:
            stack.append(int(token))

    return stack.pop()


print(evalRPN(tokens))
