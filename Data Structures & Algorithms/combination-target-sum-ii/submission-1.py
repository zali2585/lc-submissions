class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        res = [] 
        candidates.sort()

        def dfs(start, remaining):
            if remaining == 0:
                res.append(path.copy())
                return
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                dfs(i + 1, remaining - candidates[i])
                path.pop()
        dfs(0, target)
        return res