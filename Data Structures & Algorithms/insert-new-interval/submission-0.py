class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newStart, newEnd = newInterval
        i = 0
        result = []

        # adds all intervals who's end is before newInterval start 
        while i < len(intervals) and intervals[i][1] < newStart:
            result.append(intervals[i])
            i += 1

        while i < len(intervals) and intervals[i][0] <= newEnd:
            newStart = min(intervals[i][0], newStart)
            newEnd = max(intervals[i][1], newEnd)
            i += 1

        result.append([newStart, newEnd])
        while i < len(intervals):
            result.append(intervals[i])
            i+= 1
        return result
        


