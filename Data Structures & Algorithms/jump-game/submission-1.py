"""
brute force is try all subarrays and jump the maximum until you can get to the end


keep choosing what gets us the most raange till we get to the end of the array

"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = 0
        reach = 0
        jl = 0
        while reach<len(nums)-1:
            jl = nums[curr]
            reach = curr + jl
            modified = False
            for j in range(curr, reach+1):
                if reach < nums[j] + j:
                    modified = True
                    jl = nums[j]
                    reach = nums[j] + j
                    curr = j
                if j == len(nums)-1: return True
            if not modified and reach<len(nums)-1: return False
        return True