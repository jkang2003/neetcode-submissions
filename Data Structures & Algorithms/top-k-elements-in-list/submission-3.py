class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = {}
        out = []

        for i in range(len(nums)):
            if nums[i] in mydict:
                mydict[nums[i]] += 1
            else:
                mydict[nums[i]] = 1
        
        maxHeap = []

        for key in mydict:
            heapq.heappush(maxHeap, [-mydict[key], key])

        for i in range(k):
            out.append(heapq.heappop(maxHeap)[1])
        
        return out