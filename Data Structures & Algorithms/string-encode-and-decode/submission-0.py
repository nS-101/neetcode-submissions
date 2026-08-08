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
        listOfStrs = s.split(" ")
        return listOfStrs