class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path = []
        res = []
        
        def dfs(i):
            if i == len(s):
                res.append(path.copy())
            for j in range(i, len(s)):
                substring = s[i:j + 1]

                if substring == substring[::-1]:
                    path.append(substring)
                    dfs(j + 1)
                    path.pop()
        dfs(0)
        return res


