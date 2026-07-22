class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        res =[]
        used = set()

        def dfs():
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for i in range(len(nums)):
                if i in used:
                    continue
                used.add(i)
                path.append(nums[i])
                dfs()
                path.pop()
                used.remove(i)

        dfs()
        return res