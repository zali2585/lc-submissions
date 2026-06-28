# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if curr node is null, return none
        if not root:
            return None
        # swap left and right (in one line to prevent use of temp)
        root.left, root.right = root.right, root.left
        # invert left child & right child
        self.invertTree(root.left)
        self.invertTree(root.right)

        # return root of subtree/tree after done fixing
        return root
        