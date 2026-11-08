class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {"(": ")", "{": "}", "[": "]"}

        for char in s:
            if char in dic: #if it's an opener
                stack.append(char)
            else:
                if not stack: #if we have a closer with no matching opener in the stack, return false
                    return False
                elif dic[stack[-1]] != char: #if the closer doesn't match with the opener
                    return False
                else: #if the closer matches with the opener, remove the opener and clear up this match
                    stack.pop(-1)
        if len(stack) > 0: #if we still have unmatched openers, return false
            return False
        else:
            return True