"""
some type of binary search

think we can do the normal algo. if its smaller and we shift right, yet that value is smaller than the previous.... that means the array was rotated, and we instead need to shift left

and vice versa till we find the index?

"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = len(nums) - 1
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            
            if i>len(nums) and nums[i]>nums[i+1]:
                pivot = i
        
        if target>nums[pivot]:
            return -1
        elif target>nums[0]:
            #binary search in the first half
            left = 1
            right = pivot-1
            while right>=left:
                mid = (right+left)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]>target:
                    right = mid-1
                else:
                    left = mid+1
            return -1
        else:
            #binary search in the latter half
            left = pivot+1
            right = len(nums)-1
            while right>=left:
                mid = (right+left)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]>target:
                    right = mid-1
                else:
                    left = mid+1
            return -1
        