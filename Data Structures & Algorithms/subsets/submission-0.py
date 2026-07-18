class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def dfs(i):
            if i == len(nums):
                res.append(path.copy())
                return
            # include curr val and travel from there
            path.append(nums[i])
            dfs(i + 1)
            # remove inclusion to explore path where that val isnt included
            path.pop()
            # explore non inclusion path
            dfs(i + 1)

        dfs(0)
        return res