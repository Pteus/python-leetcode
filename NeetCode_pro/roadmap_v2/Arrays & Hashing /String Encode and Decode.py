from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1 + length
            res.append(s[j + 1 : i])

        return res


strs = ["neet", "code", "love", "you"]
sol = Solution()
encoded = sol.encode(strs)
decoded = sol.decode(encoded)

print(encoded)
print(decoded)
