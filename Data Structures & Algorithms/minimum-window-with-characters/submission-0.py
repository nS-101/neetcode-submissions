class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dicT = {}
        for char in t:
            dicT[char] = dicT.get(char, 0) + 1

        dicS = {}
        have = 0               # distinct letters of t currently satisfied in the window
        need = len(dicT)       # distinct letters that must be satisfied
        bestLength = float("inf")
        bestStart = 0
        left = 0

        for right in range(len(s)):
            char = s[right]
            dicS[char] = dicS.get(char, 0) + 1
            if char in dicT and dicS[char] == dicT[char]:
                have += 1

            while have == need:
                if right - left + 1 < bestLength:
                    bestLength = right - left + 1
                    bestStart = left

                leftChar = s[left]
                dicS[leftChar] -= 1
                if leftChar in dicT and dicS[leftChar] < dicT[leftChar]:
                    have -= 1
                left += 1

        return "" if bestLength == float("inf") else s[bestStart:bestStart + bestLength]