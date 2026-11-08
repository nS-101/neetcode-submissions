class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        left = 0
        dic = {}
        for right in range(len(s)):
            dic[s[right]] = dic.get(s[right], 0) + 1
            while dic[s[right]] > 1:
                dic[s[left]]-=1
                left+=1
            maxLength = max(maxLength, right-left+1)
        return maxLength