# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # hint: what path could use node as turning point
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # initializes global variable associated with object
        self.best = 0
        # helper func to calculate height from any given node
        def height(node):
            if node is None:
                return 0
                
            # gets height of subtree on left and right side
            left = height(node.left)
            right = height(node.right)
            # stores best (curr best or path from most bottom leaf node on left subtree to most bottom lead node on right subtree)
            self.best = max(self.best, left + right)
            # returns 1 + best subtree (regular height calc)
            return 1 + max(left, right)
        height(root)
        return self.best
