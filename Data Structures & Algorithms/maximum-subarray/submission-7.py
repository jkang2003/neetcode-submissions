"""
brute force
get all subarrays, sum them, and compare them to a stored max

some sort of sliding window solution
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest = nums[0]
        total = 0
        
        for i in range(len(nums)):
            if total>0:
                total+=nums[i]
                largest = max(total, largest)
            else:
                total = nums[i]
                largest = max(total, largest)
        
        return largest