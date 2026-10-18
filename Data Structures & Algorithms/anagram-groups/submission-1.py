class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []

        mydict = {}

        for i in range(len(strs)):
            signature = "".join(sorted(strs[i]))
            if signature in mydict:
                mydict[signature].append(strs[i])
            else:
                mydict[signature] = [strs[i]]

        for key in mydict:
            out.append(mydict[key])

        return out