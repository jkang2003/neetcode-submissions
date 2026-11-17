"""
approach is to create a tdict as a sort of legend
then go through s and create a dictionary only with the keys in dict
once the dictionaries are equal, then start incrementing the left window, checking that the character at the left window is not in the tdict

final string is from that left window to the last index, where the dictionaries were first made equal 


problem is that only finds the first occurrence of all the characters. if we could check for all substrings that contain all of t's chars
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        
        substrings = []
        tdict = {}
        for ch in t:
            if ch in tdict:
                tdict[ch] += 1
            else:
                tdict[ch] = 1

        sdict = {}
        left = 0
        right = 0
        while right<len(s):
            if s[right] in tdict:
                if s[right] in sdict:
                    sdict[s[right]] += 1
                else:
                    sdict[s[right]] = 1
            
            if all(sdict.get(ch, 0) >= count for ch, count in tdict.items()):
                while left<len(s):
                    if s[left] not in tdict:
                        left+=1
                    elif sdict[s[left]] > tdict[s[left]]:
                        sdict[s[left]] -= 1
                        left+=1
                    else:
                        break
                
                if not substrings:
                    substrings.append(s[left:right+1])
                    minlen = len(substrings[0])
                elif right-left+1<minlen:
                    minlen = right-left+1
                    substrings.append(s[left:right+1])

                sdict[s[left]]-=1
                left+=1

            right+=1
        
        if substrings: return min(substrings, key = len)
        return ""