class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #sorted so we use two pointers for twosum
        start = 0
        end = len(numbers)-1
        for i in range(0, len(numbers)):
            if numbers[start] + numbers[end] == target:
                return [start+1,end+1] #plus one because it is 1-indexed and not 0-indexed
            elif target > numbers[start] + numbers[end]:
                start+=1
            else: #target < numbers[start] + numbers[end]
                end-=1