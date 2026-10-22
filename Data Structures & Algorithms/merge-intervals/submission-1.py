class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        out = []
        intervals.sort()
        i = 0
        while i<len(intervals):
            merged = [intervals[i][0], intervals[i][1]]
            
            j = i+1
            while j<len(intervals) and merged[1] >= intervals[j][0]:
                merged[1] = max(merged[1], intervals[j][1])
                j+=1

            i = j
            out.append(merged)
        
        return out