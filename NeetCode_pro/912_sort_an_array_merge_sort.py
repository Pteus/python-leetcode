from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums, 0, len(nums) - 1)

    def merge_sort(self, arr, s, e):
        if e - s <= 0:
            return arr

        m = (s + e) // 2

        # Sort the left half
        self.merge_sort(arr, s, m)
        # Sort the right half
        self.merge_sort(arr, m + 1, e)
        # Merge sorted halfs
        self.merge(arr, s, m, e)

        return arr

    def merge(self, arr, s, m, e):
        # Copy the sorted left & right halfs to temp arrays
        L = arr[s : m + 1]
        R = arr[m + 1 : e + 1]

        # aux pointers
        i = 0  # for L
        j = 0  # for R
        k = s  # for arr

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


nums = [5, 1, 1, 2, 0, 0]
print(Solution().sortArray(nums))
