# https://www.youtube.com/watch?v=3OamzN90kPg

from typing import List


nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]


def containsDuplicate(nums: List[int]) -> bool:
    seen = set()

    for num in nums:
        if seen and num in seen:
            return True
        else:
            seen.add(num)
    return False


print(containsDuplicate(nums))

# time: O(n)
# space O(n)
