class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for word in strs:
            sortedword = "".join(sorted(word)) #sort the word alphabetically
            if sortedword not in dictionary:
                dictionary[sortedword] = []
            dictionary[sortedword].append(word) #key is sorted word, value is actual word in a list, so we can have multiple
        arr = []
        for value in dictionary.values():
            arr.append(value)
        return arr

