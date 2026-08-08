class Solution:

    def encode(self, strs: List[str]) -> str:
        sentence = ""
        length = len(strs)
        for index, string in enumerate(strs):
            if index == length-1:
                sentence = sentence + string 
                continue
            sentence = sentence + (string + " ")
        return sentence

    def decode(self, s: str) -> List[str]:
        if len(str) == 1:
            return list(str)
        listOfStrs = s.split(" ")
        return listOfStrs