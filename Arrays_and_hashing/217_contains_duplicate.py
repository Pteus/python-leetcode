# https://www.youtube.com/watch?v=3OamzN90kPg

nums = [1,1,1,3,3,4,3,2,4,2]

hashset = set()

for n in nums:
    if n in hashset:
        print("duplicate found:",n)
        break
        #return True
    hashset.add(n)

# time: O(n)
# space O(n)