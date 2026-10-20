class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(input, l, r):
            while l<=r:
                if input[l] != input[r]:
                    return False
                l+=1
                r-=1
            return True

        l = 0
        r = len(s) - 1
        while l<=r:
            if s[l] != s[r]:
                return is_palindrome(s, l+1,r) or is_palindrome(s,l, r-1)
            else:
                l+=1
                r-=1

        return True