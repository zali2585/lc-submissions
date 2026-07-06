# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []
        queue = deque([root])
    # allows for level_size to be recalculated for each level
        while queue:
        # calculates size of current level
            level_size = len(queue)
            # keeps going until end of this level
            for i in range(level_size):
                node = queue.popleft()
                # adding children, not considered in scope of problem yet tho
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                if i == level_size - 1:
                    res.append(node.val)
        return res
            