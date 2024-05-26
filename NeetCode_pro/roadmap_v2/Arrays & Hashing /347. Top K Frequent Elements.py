from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)  # {num:times repeated}
        freq = [[] for i in range(len(nums))]

        for num in nums:
            count[num] += 1

        for num, times in count.items():
            freq[times].append(num)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


nums = [1, 1, 1, 2, 2, 2, 3]
k = 2

print(Solution().topKFrequent(nums, k))
