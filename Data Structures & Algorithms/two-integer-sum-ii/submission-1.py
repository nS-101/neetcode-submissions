class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for index,val in enumerate(numbers):
            complement = target-val
            if complement not in hashmap:
                hashmap[val] = index
            return [hashmap[complement]+1, index+1]    
            

