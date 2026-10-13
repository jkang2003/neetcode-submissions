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
            left = [1] * len(nums)
            right = [1] * len(nums)
            for i in range(1, len(nums)):
                left[i] = nums[i-1] * left[i-1]
            for j in range(len(nums)-2, -1, -1):
                right[j] = nums[j+1] * right[j+1]
            for k in range(len(nums)):
                out[k] = left[k]*right[k]
            return out




