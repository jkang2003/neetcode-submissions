class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        chSet = set()
        l = 0

        for r in range(len(s)):
            while s[r] in chSet:
                chSet.remove(s[l])
                l+=1
            chSet.add(s[r])

            maxlen = max(maxlen, len(chSet))
        
        return maxlen