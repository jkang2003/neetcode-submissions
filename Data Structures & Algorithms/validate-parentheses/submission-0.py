class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        check = []
        for ch in s:
            if (ch == "{" or ch == "[" or ch == "("):
                check.append(ch)
            elif (ch == "}" and len(check) > 0 and check[-1] == "{"):
                check.pop()
            elif (ch == "]" and len(check) > 0 and check[-1] == "["):
                check.pop()
            elif (ch == ")" and len(check) > 0 and check[-1] == "("):
                check.pop()
            else:
                return False
        return len(check) == 0