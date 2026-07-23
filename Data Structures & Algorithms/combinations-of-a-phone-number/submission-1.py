class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # do this outside of dfs bc its not changing every recursive call 
        if not digits:
            return []

        path = []
        res = []
        hashmap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def dfs(i): 
            if i == len(digits):
                res.append("".join(path))
                return 

            for c in hashmap[digits[i]]:
                path.append(c)
                dfs(i + 1)
                path.pop()
        dfs(0)
        return res
            
