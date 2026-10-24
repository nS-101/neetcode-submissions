class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        # Pass 1: result[i] = product of everything to the LEFT of i
        leftPro = 1
        for i in range(n):
            result[i] = leftPro      # write first...
            leftPro *= nums[i]       # ...then update for the next index

        # Pass 2: multiply in the product of everything to the RIGHT of i
        rightPro = 1
        for i in range(n - 1, -1, -1):
            result[i] *= rightPro    # combine with the left part already stored
            rightPro *= nums[i]

        return result