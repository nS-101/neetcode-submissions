class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #two pointers with the smaller bar being the bottleneck, whichever pointer has the smaller bar, if we only use  that bar, then we'll only ever get the same height or lower so we change the pointer that holds the smaller bar to have the possibility of having higher water numbers
        maxWater = 0
        left = 0
        right = len(heights)-1
        currWater = 0

        while left < right:
            currWater = min(heights[left], heights[right]) ** 2 #square it since the smaller one is the bottleneck
            maxWater = max(maxWater, currWater)
            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
        
        return maxWater