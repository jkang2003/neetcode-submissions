class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [0] * len(nums)

        left = 1
        right = 1
        for i in range(len(nums)):
            out[i] = left
            left *= nums[i]

        for i in range(len(nums)-1, -1, -1):
            out[i]*=right
            right *= nums[i]

        return out


