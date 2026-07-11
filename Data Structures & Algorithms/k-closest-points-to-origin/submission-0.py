class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            if len(heap) < k:
                heapq.heappush(heap, [-distance, x, y])
            elif -distance > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, [-distance, x, y])
        return [[x, y] for _, x, y in heap]
            