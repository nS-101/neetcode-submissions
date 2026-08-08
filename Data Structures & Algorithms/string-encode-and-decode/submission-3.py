class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return None
        sentence = ""
        length = len(strs)
        for index, string in enumerate(strs):
            if index == length-1:
                sentence = sentence + string 
                continue
            sentence = sentence + (string + " ")
        return sentence

    def decode(self, s: str) -> List[str]:
        if str == None:
            return []
        listOfStrs = s.split(" ")
        return listOfStrs