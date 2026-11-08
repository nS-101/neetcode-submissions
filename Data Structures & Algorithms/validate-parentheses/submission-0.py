class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {"(": ")", "{": "}", "[": "]"}

        for char in s:
            if char in dic:
                stack.append(char)
            else:
                if dic[stack[-1]] != char:
                    return False
                else:
                    stack.pop(-1)
        if len(stack) > 0:
            return False
        else:
            return True