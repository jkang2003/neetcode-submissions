#What is the expected big O? Does case matter? Do punctuation count?
#Going to read from the end to the front of the string and compare with the front to end of the string
#Time O(n) Space O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        left = 0
        right = len(s)-1
        while left<right:
            if(s[left].isalnum() and s[right].isalnum()):
                if s[left].upper() == s[right].upper():
                    left+=1
                    right-=1
                else:
                    return False
            elif (not s[left].isalnum() and s[right].isalnum()):
                left+=1
            elif (s[left].isalnum() and not s[right].isalnum()):
                right-=1
            else:
                left+=1
                right-=1
        return True