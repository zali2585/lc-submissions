# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        # keeps rest of loop going, popping and adding right when stack gets empty 
        while curr or stack:
            # last element on curr is root, so curr.right works at end
            # keeps going until all the left most elements are added 
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            k -= 1

            if k == 0:
                return curr.val
            # once stack is empty, meaning k is greater than left subtree + 1 elems, then that mean k smallest is bigger than root so its on right
            curr = curr.right
        
