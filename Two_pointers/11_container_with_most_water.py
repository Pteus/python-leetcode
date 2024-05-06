from typing import List


heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]


def maxArea(heights: List[int]) -> int:
    max_area = 0
    l = 0
    r = len(heights) - 1

    while l < r:
        area = (r - l) * min(heights[l], heights[r])
        max_area = max(max_area, area)

        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1

    return max_area


print(maxArea(heights))
