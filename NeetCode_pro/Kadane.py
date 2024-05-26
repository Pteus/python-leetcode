# Brute force
# O(n^2)
def brute_force(nums):
    max_sum = nums[0]

    for i in range(len(nums)):
        cur_sum = 0
        for j in range(i, len(nums)):
            cur_sum += nums[j]
            max_sum = max(max_sum, cur_sum)

    return max_sum


# O(n)
def kadane(nums):
    max_sum = nums[0]
    cur_sum = 0

    for n in nums:
        cur_sum = max(cur_sum, 0)
        cur_sum += n
        max_sum = max(cur_sum, max_sum)

    return max_sum


nums = [4, -1, 2, -7, 3, 4]
print(brute_force(nums))
print(kadane(nums))
