class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxLen = 1
        numsSet = set(nums)
        for num in numsSet:
            if num-1 in numsSet:
                continue
            else:
                temp = 1
                while num+1 in numsSet:
                    temp+=1
                    num+=1
                maxLen = max(maxLen, temp)
        return maxLen