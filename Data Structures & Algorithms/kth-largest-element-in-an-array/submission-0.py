class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = []
        for n in nums:
            maxheap.append(-n)
        heapq.heapify(maxheap)
        
        for i in range(k):
            out = heapq.heappop(maxheap)
        return -out