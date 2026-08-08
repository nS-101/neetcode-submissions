class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        for index, num in enumerate(nums):
            if num not in dictionary:
                dictionary[num] = 1
            else:
                dictionary[num] += 1
        sortedDict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
        #use dictionary.items to convert dictionary to (key, value) tuples, key=lambda item:       item[1] makes it so that we sort by the values, reverse=true for sorting in descending order(highest first), dict() to wrap it all into a sorted dictionary instead of just tuples
        sortedDictKeys = list(sortedDict.keys())
        arr = []
        for i in range(k):
            if i < k:
                arr.append(sortedDictKeys[i]) #get array of highest occurring numbers 
        return arr
        
        