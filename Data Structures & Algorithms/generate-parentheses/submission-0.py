class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        res = []
        
        def dfs(openCount, closeCount):
            if openCount == closeCount == n:
                # remember sol want string, so join elems in path to string
                res.append("".join(path))
                return
            # doesn't need for loop bc at every index theres only 2 choices 
            if openCount < n:
                path.append("(")
                dfs(openCount + 1, closeCount)
                path.pop()
            # can't close a non open paran
            if closeCount < openCount:
                path.append(")")
                dfs(openCount, closeCount + 1)
                path.pop()
        dfs(0, 0)
        return res