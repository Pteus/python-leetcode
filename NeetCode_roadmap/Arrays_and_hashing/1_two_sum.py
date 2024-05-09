from typing import List


nums = [3,2,4]
target = 6

# time: O(n) - percorremos uma vez o array
# space: O(n) - o hashmap pode ser do tamanho do array 
def twoSum(nums: List[int], target: int) -> List[int]:
    prev_map = {} # value : index
    
    for i,num in enumerate(nums):
        diff = target - num
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[num] = i
    return
        


print(twoSum(nums, target))