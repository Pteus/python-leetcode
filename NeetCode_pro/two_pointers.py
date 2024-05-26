# Check if array is palindrome
def is_palindrome(arr):
    L, R = 0, len(arr) - 1

    while L < R:
        if arr[L] != arr[R]:
            return False
        L += 1
        R -= 1
    return True


arr = [1, 2, 7, 7, 2, 1]
print(is_palindrome(arr))


# Given a sorted array,return the two indices of the two elements which sums up to the target value
# Assume there is exactly on solution
def target_sum(arr, target):
    L, R = 0, len(arr) - 1

    while L < R:
        if arr[L] + arr[R] > target:
            R -= 1
        elif arr[L] + arr[R] < target:
            L += 1
        else:
            return [L, R]


arr = [-1, 2, 3, 4, 7, 9]
target = 7
print(target_sum(arr, target))
