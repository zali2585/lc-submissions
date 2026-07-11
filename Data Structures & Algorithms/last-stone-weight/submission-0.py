import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)

            if x > y: 
                y = y - x
                heapq.heappush(stones, y)
        if len(stones) == 0:
            return 0
        return stones[0] * -1
                


