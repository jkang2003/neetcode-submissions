class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = {}
        out = []

        for i in range(len(nums)):
            if nums[i] in mydict:
                mydict[nums[i]] += 1
            else:
                mydict[nums[i]] = 1
        
        occurrences = sorted(mydict, key=mydict.get, reverse=True)

        for num in occurrences:
            if len(out) < k:
                out.append(num)
        
        return out