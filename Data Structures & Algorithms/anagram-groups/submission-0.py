class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        output = []
        for i in range(len(strs)):
            check = sorted(strs[i])
            check = "".join(check)
            if check in dic:
                dic[check].append(strs[i])
            else:
                dic[check] = [strs[i]]
        
        for key in dic:
            output.append(dic[key])

        return output

