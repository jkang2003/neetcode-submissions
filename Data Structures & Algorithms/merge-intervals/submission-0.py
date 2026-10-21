class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        out = []
        intervals.sort()
        i = 0
        while i<len(intervals):
            interval = [intervals[i][0], intervals[i][1]]
            j = i+1
            while j<len(intervals) and interval[1] >= intervals[j][0]:
                interval[1] = max(interval[1], intervals[j][1])
                j+=1
            i = j
            out.append(interval)

        return out