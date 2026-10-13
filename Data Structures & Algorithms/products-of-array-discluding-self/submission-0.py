class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [0] * len(nums)
        totalproduct = 1
        zerocount = 0

        for n in nums:
            if(n != 0):
                totalproduct*=n
            else:
                zerocount+=1
                continue
        
        if zerocount>1:
            return out
        
        elif zerocount == 1:
            for i in range(len(nums)):
                if(nums[i] != 0):
                    out[i] = 0
                else:
                    out[i] = totalproduct
            return out
        
        else:
            for i in range(len(nums)):
                out[i] = int(totalproduct/nums[i])
            return out