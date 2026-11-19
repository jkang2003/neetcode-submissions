"""
Same idea as previous. some sort of binary search, discarding where the target could not possibly be.

The minimum in this case is literally the drop in the array

So if we know a side is sorted, we can discard that side

And continue doing so until we get to the drop. Will figure out what kind of implementation that entails. Gonna start with a skeleton first
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        small = nums[l]

        while l<=r:
            mid = (l+r)//2
            small = min(nums[mid], small)

            if nums[mid]<nums[r]:
                r = mid-1
            else:
                l = mid+1

        
        return small