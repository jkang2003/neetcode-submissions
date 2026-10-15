class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chSet = set()
        left = 0
        res = 0
        for right in range(len(s)):
            while s[right] in chSet:
                chSet.remove(s[left])
                left+=1
            chSet.add(s[right])
            res = max(res, right-left+1)
        return res
