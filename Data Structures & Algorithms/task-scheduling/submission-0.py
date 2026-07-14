from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        count = Counter(tasks)
        heap = [-freq for freq in count.values()]
        heapq.heapify(heap)
        queue = deque()

        while heap or queue:

            if not heap:
                time = queue[0][1] - 1
            
            time += 1

            while queue and queue[0][1] <= time:
                taskCount, availableTime = queue.popleft()
                heapq.heappush(heap, taskCount)
            
            if heap:
                taskCount = heapq.heappop(heap)
                taskCount += 1
                availableAgain = time + n + 1
                if taskCount != 0:
                    queue.append((taskCount, availableAgain))
        return time


                

