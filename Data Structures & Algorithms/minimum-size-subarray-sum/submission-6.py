class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = 0
        l = 0
        minlen = None

        for i in range(len(nums)):
            sum+=nums[i]
            while sum>=target:
                if minlen:
                    minlen = min(minlen, i-l+1)
                else:
                    minlen = i-l+1
                sum-=nums[l]
                l+=1
                
        if minlen: return minlen
        return 0