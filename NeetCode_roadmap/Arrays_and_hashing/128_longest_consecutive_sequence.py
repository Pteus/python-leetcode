from typing import List


nums = [100, 4, 200, 1, 3, 2]


def longestConsecutive(nums: List[int]) -> int:
    numSet = set(nums)
    longest = 0

    for n in nums:
        if (n - 1) not in numSet:
            length = 0
            while (n + length) in numSet:
                length += 1
            longest = max(longest, length)

    return longest


# Time O(n)
# Space O(n) -> we creted a set -> size of the input array

print(longestConsecutive(nums))
