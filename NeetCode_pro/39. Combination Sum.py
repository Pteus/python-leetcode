from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, curr_sum):
            # base cases
            if curr_sum == target:
                res.append(subset.copy())
                return
            if curr_sum > target or i > len(candidates):
                return

            subset.append(candidates[i])
            dfs(i + 1, curr_sum + candidates[i])

            subset.pop()
            dfs(i + 1, curr_sum)

        dfs(0, 0)
        return res


candidates = [2, 3, 6, 7]
target = 7

print(Solution().combinationSum(candidates, target))
