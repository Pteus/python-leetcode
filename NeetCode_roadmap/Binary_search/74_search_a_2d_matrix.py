from typing import List


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    ROWS = len(matrix)
    COLS = len(matrix[0])

    top = 0
    bottom = ROWS - 1

    while top <= bottom:
        row = (top + bottom) // 2

        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bottom = row - 1
        else:
            break

    if not (top <= bottom):
        return False

    l = 0
    r = COLS - 1

    while l <= r:
        m = (l + r) // 2
        if target > matrix[row][m]:
            l = m + 1
        elif target < matrix[row][m]:
            r = m - 1
        else:
            return True

    return False


print(searchMatrix(matrix, target))
