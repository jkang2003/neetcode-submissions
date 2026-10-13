class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        count = 1
        mlen = 1
        checks = set(nums)

        for check in checks:
            if check - 1 not in checks:
                while check + 1 in checks:
                    count += 1
                    check += 1
                    mlen = max(count, mlen)
                count = 1
        return mlen