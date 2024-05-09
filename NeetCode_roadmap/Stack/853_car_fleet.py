from typing import List

target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]


def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    pair = [[p, s] for p, s in zip(position, speed)]
    stack = []

    for p, s in sorted(pair, reverse=True):
        stack.append((target - p) / s)
        if len(stack) >= 2 and stack[-2] >= stack[-1]:
            stack.pop()

    return len(stack)


# time: O(nlogn) porque tivemos que fazer um sort
# space: O(n) porque usamos uma stack que pode crescer até ao tamanho max de carros caso nao haja colisoes

print(carFleet(target, position, speed))
