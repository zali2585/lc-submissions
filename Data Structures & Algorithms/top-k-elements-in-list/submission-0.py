class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        vals = list(freq.items())
        vals.sort(key = lambda x : x[1])
        vals.reverse()
        return list(x for x,y in vals[:k])
        