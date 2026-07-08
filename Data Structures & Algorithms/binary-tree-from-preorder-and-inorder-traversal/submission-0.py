# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # main idea: root is first in preorder and in in order, everything to left of it is in left sub tree and everything to right is in right subtree
        # break the lists up and pass in smaller params each time

        inorder_index = {val: i for i, val in enumerate(inorder)}
        # marks root index
        # has to be non-local so not recreated each recursion
        pre_i = 0
        # passes in left and right index of tree array to build
        def build(left, right):
            nonlocal pre_i
            # not >= bc if = that means array is 1 element [9] and thats valid 
            if left > right:
                return None
            # set root to preorder index
            root_val = preorder[pre_i]
            # increments to next root index (left root)
            pre_i += 1
            # creates node for root
            root = TreeNode(root_val)
            # retrieves index for root
            mid = inorder_index[root_val]
            # builds left tree from beginning till root
            root.left = build(left, mid - 1)
            # builds right tree from root to right (not including root)
            root.right = build(mid + 1, right)

            return root
        return build(0, len(inorder) - 1)

