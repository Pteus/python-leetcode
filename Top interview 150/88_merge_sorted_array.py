from typing import List

nums1 = [1, 2, 3, 0, 0, 0]
m = 3  # number of non zero values on nums1 list
nums2 = [2, 5, 6]
n = 3


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    last = len(nums1) - 1

    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[last] = nums1[m - 1]
            m -= 1
        else:
            nums1[last] = nums2[n - 1]
            n -= 1
        last -= 1

    while n > 0:
        nums1[last] = nums2[n - 1]
        n -= 1
        last -= 1


merge(nums1, m, nums2, n)

print(nums1)
