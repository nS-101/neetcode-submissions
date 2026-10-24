class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1 #frequency map of numbers
        sortedTuples = sorted(hashmap.items(), key=lambda item: item[1], reverse = True) #convert dictionary into a list of sorted tuples(sorted by values in decreasing order meaning numbers most frequent are first)
        arr = []
        for i in range(0,k):
            arr.append(sortedTuples[i][0]) #add k most frequent numbers to list that will be returned
        return arr