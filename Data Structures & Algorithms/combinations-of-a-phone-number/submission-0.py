class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
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
            if not digits:
                return []
            if i == len(digits):
                res.append("".join(path))
                return 
            num = digits[i]

            for c in hashmap[num]:
                path.append(c)
                dfs(i + 1)
                path.pop()
        dfs(0)
        return res
            
