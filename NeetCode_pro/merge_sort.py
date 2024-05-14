from typing import List


class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value


class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.merge_sort_helper(pairs, 0, len(pairs) - 1)

    def merge_sort_helper(self, pairs, s, e):
        if e - s + 1 <= 1:
            return pairs

        # find the middle
        m = (s + e) // 2

        # sort the left half
        self.merge_sort_helper(pairs, s, m)
        # sort the right half
        self.merge_sort_helper(pairs, m + 1, e)
        # merge
        self.merge(pairs, s, m, e)

        return pairs

    def merge(self, arr, s, m, e):
        L = arr[s : m + 1]
        R = arr[m + 1 : e + 1]

        i = 0  # index for L
        j = 0  # index for R
        k = s  # index for arr

        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # one side will still have something
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
