class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = {}
        left = 0
        bestLength = 0
        for right in range(len(s)):
            charCount[s[right]] = charCount.get(s[right], 0) + 1
            while (right-left+1) - max(charCount.values()) > k:   # replacements needed for the current window
                charCount[s[left]] -= 1
                left += 1
            bestLength = max(bestLength, right - left + 1)
        return bestLength
