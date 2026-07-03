# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(p, q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            if p.val != q.val:
                return False
            return (sameTree(p.left, q.left) and sameTree(p.right, q.right))
        # if subtree empty, vacuously true that subtree is in tree bc null is always a part of tree
        if subRoot is None:
            return True
        # if root is none and subroot isnt, false bc no matching node found
        if root is None:
            return False
        # sameTree checks if roots are equal and all descedant nodes
        # if so, return true
        if sameTree(root, subRoot):
            return True
        # recursively calls on left and right
        # if even one is subtree, return true bc u only need one 
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
