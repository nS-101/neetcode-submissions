class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest = 0
        left = 0
        
        for right in range(len(prices)):
            if prices[right] < prices[left]:
                left = right
            highest = max(highest, prices[right]-prices[left])
        
        return highest
