from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if seen and num in seen:
                return True
            else:
                seen.add(num)
        return False


nums = [1, 2, 3, 1]

print(Solution().containsDuplicate(nums))
