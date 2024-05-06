from typing import List


nums = [-1, 0, 3, 5, 9, 12]
target = 9


def search(nums: List[int], target: int) -> int:
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = (l + r) // 2

        if target < nums[m]:
            r = m - 1
        elif target > nums[m]:
            l = m + 1
        else:
            return m

    return -1


# time : O(logn)
# space: O(1)


print(search(nums, target))


# _ _ _ _ _
# l   m    r
