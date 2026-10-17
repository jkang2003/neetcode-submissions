class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        
        heapq.heapify(stones)

        while len(stones)>1:
            big = heapq.heappop(stones)
            small = heapq.heappop(stones)
            heapq.heappush(stones, big-small)

        return -1*heapq.heappop(stones)