# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, upper, lower):
            if node is None:
                return True
            # check if curr node follows rules of bounds
            if not (lower < node.val < upper):
                return False
            # return if right sub tree and left subtree are valid both
            return (
                valid(node.left, node.val, lower)
                and valid(node.right, upper, node.val))
        return valid(root, float("inf"), float("-inf"))