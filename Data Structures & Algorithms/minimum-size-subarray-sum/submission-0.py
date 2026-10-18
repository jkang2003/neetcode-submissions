class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        out = None
        total = 0
        r = 0

        for i in range(0, len(nums)):
            while total<target and r<len(nums):
                total+=nums[r]
                r+=1
            if out and target<=total:
                out = min(out, r-i)
            elif not out and target<=total:
                out = r-i
            total-=nums[i]

        if not out: return 0
        return out