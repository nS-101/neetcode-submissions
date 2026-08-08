class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        found = False
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                found = True
        return found