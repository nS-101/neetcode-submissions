class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for word in strs:
            sortedword = "".join(sorted(word)) #sort the word alphabetically
            if sortedword not in dictionary:
                dictionary[sortedword] = []
            dictionary[sortedword].append(word) #key is sorted word, value is list, so we can have multiple words corresponding to sorted word
        arr = []
        for value in dictionary.values():
            arr.append(value)
        return arr

