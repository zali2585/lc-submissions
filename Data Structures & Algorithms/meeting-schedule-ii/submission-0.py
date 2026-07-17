"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda i: i.start)

        heap = []
        for i in intervals:
            if heap and i.start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, i.end)

        return len(heap)

