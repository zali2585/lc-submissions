# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxSoFar):
            if node is None:
                return 0
            count = 0 
            if node.val >= maxSoFar:
                count = 1
                maxSoFar = node.val
            leftCount = dfs(node.left, maxSoFar)
            rightCount = dfs(node.right, maxSoFar)

            return count + leftCount + rightCount
        return dfs(root, float("-inf"))
            
