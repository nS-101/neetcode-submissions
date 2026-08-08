class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #optimal solution to twosum is using a hash/dict
        seenNumbers = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in seenNumbers:
                return [seenNumbers[complement], index] #return the indexes, smaller first
            seenNumbers[num] = index #add new keyvalue pair to dict
        return [] #return empty array for no solution