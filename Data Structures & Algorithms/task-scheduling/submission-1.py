class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxFreq = max(count.values())

        numMaxFreqTasks = 0
        for val in count.values():
            if val == maxFreq:
                numMaxFreqTasks += 1
        
        return max(len(tasks), (maxFreq - 1) * (n + 1) + numMaxFreqTasks)