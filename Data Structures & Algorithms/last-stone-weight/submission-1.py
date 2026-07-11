import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        # remember, y is guaranteed >= x, so y will always be bigger=
        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            # need to flip because its negative 
            if x != y: 
                heapq.heappush(stones, y - x)
        return -stones[0] if stones else 0
                
# runtime: O(n log n)
# heapify = O(n), pop & push = O(log n )

