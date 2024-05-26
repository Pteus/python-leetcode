from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # # solution 1
        # # T: O(nlogn)
        # # S: O(n)
        # return sorted(s) == sorted(t)

        # # Solution 2
        # # T: O(s+t)
        # # S: O(s+t)
        # return Counter(s) == Counter(t)

        # Solution 3
        # time: O(s+t)
        # space: O(s+t)
        # if the string have different sizes they are not anagrams
        if len(s) != len(t):
            return False

        count_s, count_t = {}, {}
        # since they are the same size we can use it to create the for loop
        for i in range(len(s)):
            count_t[t[i]] = count_t.get(t[i], 0) + 1
            count_s[s[i]] = count_s.get(s[i], 0) + 1

        return count_t == count_s


s = "anagram"
t = "nagaram"
print(Solution().isAnagram(s, t))
