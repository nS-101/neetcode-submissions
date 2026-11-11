class Solution:
    def isValid(self, s: str) -> bool:
        #monotonic stack problem

        stack = []
        dic = {"(": ")", "{": "}", "[": "]"}

        for char in s:
            if char in dic: #if it is an opener
                stack.append(char)
            else:
                if not stack: #if stack is empty, meaning no matching opener to this closer
                    return False
                elif dic[stack[-1]] != char:
                    return False
                else:
                    stack.pop(-1)
        
        if len(stack) > 0: #if the stack isn't empty, there are unmatched openers, so return False
            return False
        return True #at this point, it means the stack is empty so everything was matched