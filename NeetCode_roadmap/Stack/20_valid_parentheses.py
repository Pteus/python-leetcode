s = "(){}"


def isValid(s: str) -> bool:
    stack = []
    close_to_open_map = {")": "(", "]": "[", "}": "{"}

    for c in s:
        if c in close_to_open_map:  # se é a fechar
            if stack and stack[-1] == close_to_open_map[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    return not stack


# time: O(n) -> so percorremos a string uma vez
# space: O(n) -> estamos a usar uma stack que pode ser do tamanho da string

print(isValid(s))
