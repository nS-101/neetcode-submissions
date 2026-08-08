class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        arr = list(s)
        arr2 = list(t)
        
        arr.sort()
        arr2.sort()
        for i in range(len(arr)):
            if arr[i] != arr2[i]:
                return False
        return True