class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVol = 0
        l = 0
        r = len(heights) - 1
        i = 1

        while(l<r):
            maxVol = max((min(heights[l],heights[r]) * abs(r-l)), maxVol)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        
        return maxVol
            