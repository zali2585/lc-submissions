# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None:
                return True, 0
            leftBalanced, leftHeight = dfs(node.left)
            rightBalanced, rightHeight = dfs(node.right)

            balanced = (leftBalanced and rightBalanced and abs(leftHeight - rightHeight) <= 1)
            height = max(leftHeight, rightHeight) + 1
            return balanced, height
        balanced, height = dfs(root)
        return balanced