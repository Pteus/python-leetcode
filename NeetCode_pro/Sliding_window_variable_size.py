nums = [4, 2, 2, 3, 3, 3]


# Find the length of the longest subarray, with the same value in each position
# O(n)
def longest_subarray(nums):
    L, length = 0, 0

    for R in range(len(nums)):
        if nums[L] != nums[R]:
            L = R
        length = max(length, R - L + 1)

    return length


print(longest_subarray(nums))


# Find the minimum length subarray where the sum is greater than or igual to the target.
# Assume all values are positive
nums = [2, 3, 1, 2, 4, 3]
target = 6


def shortest_subarray(nums, target):
    L, total = 0, 0
    length = float("inf")

    for R in range(len(nums)):
        total += nums[R]
        while total >= target:
            length = min(R - L + 1, length)
            total -= nums[L]
            L += 1
    return 0 if length == float("inf") else length


print(shortest_subarray(nums, target))
