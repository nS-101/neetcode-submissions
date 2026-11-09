class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = {}
        left = 0
        bestLength = 0
        for right in range(len(s)):
            charCount[s[right]] = charCount.get(s[right], 0) + 1
            while (right-left+1) - max(charCount.values()) > k:   #this formula compares the usage of k by extracting the amount of characters we have used k on(aren't the highest ocurring character) and shrinking whenever this amount exceeds k
                charCount[s[left]] -= 1
                left += 1
            bestLength = max(bestLength, right - left + 1)
        return bestLength
