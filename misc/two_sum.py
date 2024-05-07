from typing import List


nums = [3, 2, 4]
target = 6
# Output: [1,2]


def twoSum(nums: List[int], target: int) -> List[int]:
    values_map = {}  # num: index

    for i, num in enumerate(nums):
        diff = target - num
        if diff in values_map:
            return [values_map[diff], i]
        values_map[num] = i


print(twoSum(nums, target))
