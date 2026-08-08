class Solution:

    def encode(self, strs: List[str]) -> str:
        sentence = ""
        length = len(strs)
        for index, string in enumerate(strs):
            # Use a delimiter that includes the length to handle spaces/empty strings
            sentence = sentence + str(len(string)) + ":" + string
        return sentence

    def decode(self, s: str) -> List[str]:
        listOfStrs = []
        i = 0
        while i < len(s):
            # Find the position of the delimiter
            j = s.find(":", i)
            # Extract the length of the next string
            length = int(s[i:j])
            # Extract the string based on the length
            listOfStrs.append(s[j+1:j+1+length])
            i = j + 1 + length
        return listOfStrs