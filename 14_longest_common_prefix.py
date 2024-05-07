from typing import List


strs = ["flower", "flow", "flight"]


def longestCommonPrefix(strs: List[str]) -> str:
    res = ""
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return res
        res += strs[0][i]

    return res


print(longestCommonPrefix(strs))
