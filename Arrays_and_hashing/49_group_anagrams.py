from collections import defaultdict
from typing import List

strs = ["eat","tea","tan","ate","nat","bat"]

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    res = defaultdict(list)

    for s in strs:
        count = [0] * 26 # a...z sao 26 caracteres, este array serve para contar quantas occurencias do caracter existe
        
        for c in s:
            count[ord(c) - ord("a")] += 1
            
        res[tuple(count)].append(s)
    
    #print(res)
    return res.values()
            
print(groupAnagrams(strs))

# time O(m.n) 
# space O(1) constant