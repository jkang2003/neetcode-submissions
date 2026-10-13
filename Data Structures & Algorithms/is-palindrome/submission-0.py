#What is the expected big O? Does case matter? Do punctuation count?
#Going to read from the end to the front of the string and compare with the front to end of the string
#Time O(n) Space O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return true
        
        comp = ""
        for ch in s:
            if ch.isalnum():
                comp += ch
        
        normalized = comp.upper()
        return normalized == normalized[::-1]