class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones)>1:
            stones.sort(reverse = True)
            temp = stones[1]
            stones.remove(stones[1])
            stones[0] -= temp
        
        return stones[0]