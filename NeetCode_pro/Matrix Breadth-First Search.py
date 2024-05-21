from collections import deque
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        # number os rows and columns
        ROWS, COLS = len(grid), len(grid[0])
        # a set to save the visited coordinates
        visit = set()
        # a queue for the bfs
        queue = deque()

        # add the starting position
        visit.add((0, 0))
        queue.append((0, 0))

        length = 0

        # while we have something in the queue
        while queue:
            for i in range(len(queue)):
                # pop it and assign the respective coordinates to r and c
                r, c = queue.popleft()

                # reached the end of the grid
                if r == ROWS - 1 and c == COLS - 1:
                    return length

                search_directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

                for dr, dc in search_directions:
                    search_row = r + dr
                    search_col = c + dc

                    # check if out of bounds
                    # check if already visited
                    # check if it's a blocked position (value == 1)
                    if (
                        min(search_row, search_col) < 0
                        or search_row == ROWS
                        or search_col == COLS
                        or (search_row, search_col) in visit
                        or grid[search_row][search_col] == 1
                    ):
                        continue

                    queue.append((search_row, search_col))
                    visit.add((search_row, search_col))

            length += 1
        return -1


grid = [[0, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0]]

print(Solution().shortestPath(grid))
