class Solution:
    #used claude for, this, quite tricky

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            newWord = str(len(word)) + "#" + word
            result+=newWord
        return result
            
        

    def decode(self, s: str) -> List[str]:
        arr = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            start = j + 1
            end = start + length
            word = s[start:end]
            arr.append(word)
            i = end
        return arr
            