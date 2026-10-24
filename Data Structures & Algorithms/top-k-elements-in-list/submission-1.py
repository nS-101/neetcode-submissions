class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1 #frequency map of numbers
        sortedTuples = sorted(hashmap.items(), key=lambda item: item[1], reverse = True)
        arr = []
        for i in range(0,k):
            arr.append(sortedTuples[i][0])
        return arr