class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        hashmap2 = {}
        for i in range(0, len(s)):
            hashmap[s[i]] = hashmap.get(s[i], 0) + 1 #create key for it if it's a new character and if not, update existing key
        for i in range(0, len(t)):
            hashmap2[t[i]] = hashmap2.get(t[i], 0) + 1
        if hashmap == hashmap2:
            return True
        return False