from typing import List


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        return self._dfs(grid, 0, 0, set())

    def _dfs(self, grid: List[List[int]], r: int, c: int, visit: set) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        # check if out of bounds
        # check if already visited
        # check if it's a blocked position (value == 1)
        if (
            min(r, c) < 0
            or r == ROWS
            or c == COLS
            or (r, c) in visit
            or grid[r][c] == 1
        ):
            return 0

        # check if we reached the end of the matrix (3,3)
        if r == ROWS - 1 and c == COLS - 1:
            return 1

        # mark this r,c as visited on this path
        visit.add((r, c))

        count = 0
        # recursive dfs on 4 directions
        count += self._dfs(grid, r + 1, c, visit)
        count += self._dfs(grid, r - 1, c, visit)
        count += self._dfs(grid, r, c + 1, visit)
        count += self._dfs(grid, r, c - 1, visit)

        # need to remove from visited so that on the next path this r,c is allowed to be passed
        visit.remove((r, c))

        return count


grid = [[0, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0]]

print(Solution().countPaths(grid))
