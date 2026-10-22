class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        totalproduct = 1
        zerocount = 0
        for num in nums:
            if num == 0:
                zerocount+=1
                continue
            totalproduct*=num
        
        if zerocount>1:
            return [0]*len(nums)
        
        elif zerocount == 1:
            for i in range(len(nums)):
                if nums[i] != 0:
                    out.append(0)
                else:
                    out.append(totalproduct)
        else:
            for i in range(len(nums)):
                out.append(totalproduct//nums[i])

        return out



