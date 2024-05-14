from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            j = i - 1
            while j >= 0 and nums[j + 1] < nums[j]:
                nums[j + 1], nums[j] = nums[j], nums[j + 1]
                j -= 1

        return nums


nums = [5, 1, 1, 2, 0, 0]
print(Solution().sortArray(nums))
