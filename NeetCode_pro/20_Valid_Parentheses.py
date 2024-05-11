s = "()[]{}"


def isValid(s: str) -> bool:
    open_to_closed_map = {"(": ")", "[": "]", "{": "}"}
    stack = []

    for c in s:
        if c in open_to_closed_map:  # it's an openning parenthesis
            stack.append(c)
        else:
            if stack and open_to_closed_map[stack[-1]] == c:
                stack.pop()
            else:
                return False

    return not stack


# time: O(n) -> so percorremos a string uma vez
# space: O(n) -> estamos a usar uma stack que pode ser do tamanho da string

print(isValid(s))
