class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # sorting so that our left and right pointer can move based on an ordered list
        out = [] #our list which will store our tuples

        for i in range(len(nums)): #iterate through the list, chooseing i as our first value in the tuple.
            if(i>0 and nums[i] == nums[i-1]): #if we've used this value as our first value in a tuple, skip it
                i+=1
                continue

            left = i+1 #left pointer is one to the right of i, since i starts at the beginning of the list and iterates to the end
            right = len(nums) - 1 #right pointer is the last element since its the largest

            while left<right: #while our pointers dont cross
                if nums[i] + nums[left] + nums[right] == 0: #working tuple, then append it
                    out.append([nums[i], nums[left], nums[right]])
                    left+=1 #increment left to search for more tuples
                    while(nums[left] == nums[left-1] and left<right): #until the left is not the same as the last left ie the second value in the tuple at this i is not the same, keep incrementing
                        left+=1
                elif nums[i] + nums[left] + nums[right] < 0: #triplet is too small, increment left
                    left+=1
                else: #else decrement right. since neither our first or our second tuple can be the same value, the right cannot be the same either. so no need to account for duplicates here, as a duplicate would just get decremented again
                    right-=1

        return out