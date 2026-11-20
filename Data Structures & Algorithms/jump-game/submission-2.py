"""
brute force is try all subarrays and jump the maximum until you can get to the end


keep choosing what gets us the most raange till we get to the end of the array

"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for i in range(len(nums)):
            if i > reach:
                return False
            reach = max(reach, i + nums[i])
        return True
