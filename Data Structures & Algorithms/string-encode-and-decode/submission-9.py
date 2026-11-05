class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for i in range(len(strs)):
            out += str(len(strs[i])) + "#" + strs[i]
        return out 

    def decode(self, s: str) -> List[str]:
        out = []
        i = 0
        while i<len(s):
            strlen = ""
            while i<len(s) and s[i].isdigit():
                strlen+=s[i]
                i+=1
            
            currlen = int(strlen)

            if s[i] == "#":
                word = ""
                j = i+1
                while j<len(s) and j < i+1+currlen:
                    word+=s[j]
                    j+=1
                i = j - 1
                out.append(word)
            i+=1
        return out