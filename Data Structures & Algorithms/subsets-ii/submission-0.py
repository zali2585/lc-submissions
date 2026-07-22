class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        used = set()
        nums.sort()
       
        def dfs(i):
            res.append(path.copy())
        
            for j in range(i, len(nums)):
                if j in used:
                    continue
                if j > i and nums[j] == nums[j - 1]:
                    continue
                path.append(nums[j])
                used.add(j)
                dfs(j + 1)
                used.remove(j)
                path.pop()
        dfs(0)
        return res
        
