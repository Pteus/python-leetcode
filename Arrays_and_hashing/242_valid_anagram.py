from collections import Counter


s = "anagram"
t = "nagaram"

# # Solution 1 - hashmaps/dicionarios e contar cada occurencia de cada letra
# # time: O(s+t)
# # space: O(s+t)
# def isAnagram(s: str, t: str) -> bool:
#     if len(s) != len(t):
#         return False

#     count_s, count_t = {},{}

#     for i in range(len(s)):
#         count_s[s[i]] = 1 + count_s.get(s[i],0) # o caracter pode ainda nao existir no dic 
#         count_t[t[i]] = 1 + count_t.get(t[i],0) # o caracter pode ainda nao existir no dic 

#     for c in count_s:
#         if count_s[c] != count_t.get(c,0):
#             return False
    
#     return True

# # Solution 2 - Usar o Counter
# # time: O(s+t)
# # space: O(s+t)
# def isAnagram(s: str, t: str) -> bool:
#     return Counter(s) == Counter(t)

# Solution 3
# time:  O(n^2) bubble sort, ou O(nlog(n))
# space: O(1) Alguns entrevistadores assumem que sort = O(1)
def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

print("is anagram:", isAnagram(s,t))





