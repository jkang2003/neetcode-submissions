class Solution:
    """
    we can walk through the by ch
    track a current ch

    build a substring based off ch, swapping to ch if we havent hit the k limit
    track length at each iteration and compare to a stored max

    return the max

    longest = 1
        check = s[0]
        limit = 0
        sublen = 0

        for ch in s:
            if ch == check:
                sublen += 1
                longest = max(sublen, longest)
            elif ch != check and limit<k:
                limit += 1
                sublen += 1
                longest = max(sublen, longest)
            else:
                longest = max(sublen, longest)
                check = ch
                sublen = 1
                limit = 0
        
        return longest

    approach above fails on cases where replacement is not linear/we walk past chosen ch

    """
    def characterReplacement(self, s: str, k: int) -> int:
        chcounts = {}
        maxlen = 0
        left = 0
        right = 0
        while right<len(s) and left<=right:
            sublen = right-left+1
            if s[right] in chcounts:
                chcounts[s[right]] += 1
            else:
                chcounts[s[right]] = 1
            
            if sublen - k <= max(chcounts.values()):
                maxlen = max(sublen, maxlen)
            else:
                chcounts[s[left]] -= 1 
                left+=1
                
            right+=1
        
        return maxlen