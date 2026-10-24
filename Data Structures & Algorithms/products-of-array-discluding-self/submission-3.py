class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftRow = [1] * n
        rightRow = [1] * n

        snowball = 1
        for i in range(n):
            leftRow[i] = snowball
            snowball *= nums[i]

        snowball = 1
        for i in range(n - 1, -1, -1):
            rightRow[i] = snowball
            snowball *= nums[i]

        result = []
        for i in range(n):
            result.append(leftRow[i] * rightRow[i])
        return result