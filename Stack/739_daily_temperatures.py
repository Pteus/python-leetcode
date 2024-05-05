from typing import List


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    res = [0] * len(temperatures)
    stack = []  # pair: [temperature, index]

    for i, t in enumerate(temperatures):

        while stack and t > stack[-1][0]:
            stack_temp, stack_index = stack.pop()
            res[stack_index] = i - stack_index

        stack.append([t, i])

    return res


print(dailyTemperatures(temperatures))
