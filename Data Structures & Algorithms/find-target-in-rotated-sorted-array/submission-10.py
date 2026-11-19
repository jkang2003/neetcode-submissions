"""
some type of binary search

think we can do the normal algo. if its smaller and we shift right, yet that value is smaller than the previous.... that means the array was rotated, and we instead need to shift left

and vice versa till we find the index?

"""

"""
Plan as comments: one line each for "check mid," "find which half is sorted," and "is the target in that half?"
"Plan is X, cost Y," out loud or typed here.
Code, then trace it on [4,5,6,7,0,1,2] with target = 0 and target = 3.
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            # left half [l..mid] is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1      # target is inside the sorted left half
                else:
                    l = mid + 1      # it's not, so go right
            # otherwise right half [mid..r] is sorted
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1      # target is inside the sorted right half
                else:
                    r = mid - 1      # it's not, so go left

        return -1
