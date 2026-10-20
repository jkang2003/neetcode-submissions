class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        out = []
        pdict = {}
        for ch in p:
            if ch in pdict:
                pdict[ch] += 1
            else:
                pdict[ch] = 1

        segment = s[0:len(p)]
        segdict = {}
        for ch in segment:
            if ch in segdict:
                segdict[ch] += 1
            else:
                segdict[ch] = 1
        
        if segdict == pdict: out.append(0)
        left = 0

        for i in range(1, len(s) - len(p) + 1):
            if segdict[s[left]] > 1: segdict[s[left]] -= 1
            else: segdict.pop(s[left], 1)
            left+=1
            if s[i + len(p) - 1] in segdict:
                segdict[s[i + len(p) - 1]] += 1
            else:
                segdict[s[i + len(p) - 1]] = 1

            if segdict == pdict: out.append(i)

        return out