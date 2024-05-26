from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_nums = {}  # {diff,index}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in prev_nums:
                return [i, prev_nums[diff]]
            prev_nums[num] = i


nums = [2, 7, 11, 15]
target = 9

print(Solution().twoSum(nums, target))
