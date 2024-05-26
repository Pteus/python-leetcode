# Brute force
# O(n*k)


def brute_force(nums, k):
    for L in range(len(nums)):
        for R in range(L + 1, min(len(nums), L + k)):
            if nums[L] == nums[R]:
                return True
    return False


# O(n)
def close_duplicates(nums, k):
    window = set()
    L = 0

    for R in range(len(nums)):
        if R - L + 1 > k:
            window.remove(nums[L])
            L += 1
        if nums[R] in window:
            return True
        window.add(nums[R])

    return False


nums = [1, 2, 3, 4, 3, 4]
k = 3

print(brute_force(nums, k))
print(close_duplicates(nums, k))
