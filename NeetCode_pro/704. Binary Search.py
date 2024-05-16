from typing import List


nums = [-1, 0, 3, 5, 9, 12]
target = 2


def search(nums: List[int], target: int) -> int:
    L = 0
    R = len(nums) - 1

    while L <= R:
        mid = (L + R) // 2

        if nums[mid] < target:
            L += 1
        elif nums[mid] > target:
            R -= 1
        else:
            return mid

    return -1


# time : O(logn)
# space: O(1)


print(search(nums, target))


# _ _ _ _ _
# l   m    r
