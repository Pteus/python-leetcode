from typing import List


input = ["neet", "code", "loves", "you"]


def encode(strs: List[str]) -> str:
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res


def decode(s: str) -> List[str]:
    res = []
    i = 0

    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i:j])
        res.append(s[j + 1 : j + 1 + length])
        i = j + 1 + length

    return res


encoded = encode(input)
decoded = decode(encoded)
print(encoded)
print(decoded)
