class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        for ch in s:
            if ch in dict:
                dict[ch] +=1
            else:
                dict[ch] = 1
        
        dict2 = {}
        for ch in t:
            if ch in dict2:
                dict2[ch] +=1
            else:
                dict2[ch] = 1

        return dict == dict2