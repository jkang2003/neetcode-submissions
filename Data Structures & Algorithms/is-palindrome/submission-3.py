#What is the expected big O? Does case matter? Do punctuation count?
#Going to read from the end to the front of the string and compare with the front to end of the string
#Time O(n) Space O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        
        S = s.upper()
        left = 0
        right = len(s)-1
        while left<right:
            if(S[left].isalnum() and S[right].isalnum()):
                if S[left] == S[right]:
                    left+=1
                    right-=1
                else:
                    return False
            elif (not S[left].isalnum() and S[right].isalnum()):
                left+=1
            elif (S[left].isalnum() and not S[right].isalnum()):
                right-=1
            else:
                left+=1
                right-=1
        return True