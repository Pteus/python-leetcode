from collections import defaultdict
from typing import List

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  # {tuple(count) : [words]}

        for s in strs:
            count = [0] * 26  # 26 lowercase english letters

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)
        return res.values()


print(Solution().groupAnagrams(strs))
