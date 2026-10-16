class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = len(nums)
        numsum = 0
        for i in range(len(nums)):
            sum+=i
            numsum+=nums[i]
        
        return sum-numsum
        