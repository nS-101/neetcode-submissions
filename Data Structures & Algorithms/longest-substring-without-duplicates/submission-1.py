class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window since we want the longest substring that has no duplicates(string within a string means sliding window to find that substring)
        maxLength = 0
        left = 0
        dic = {} #frequency map for characters to see if we have a duplicate or not
        for right in range(len(s)):
            dic[s[right]] = dic.get(s[right], 0) + 1 #add occurrence to frequency map
            while dic[s[right]] > 1: #while we have a duplicate for the current character, shrink window from left until there are no duplicates any more 
                dic[s[left]]-=1 #reduce count since these are leaving the window
                left+=1 #window shrinks so left increases
            maxLength = max(maxLength, right-left+1) #track biggest size of window with no duplicates
        return maxLength