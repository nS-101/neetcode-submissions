class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #sliding window since we want to maximize difference between left and right side within list
        highest = 0
        left = 0
        
        for right in range(len(prices)):
            if prices[right] < prices[left]: #if we see a cheaper buy than what we have set left to that
                left = right
            highest = max(highest, prices[right]-prices[left]) #get highest possible difference between left and right
        
        return highest
