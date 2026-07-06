# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # creates list of results 
        res = []
        # helper function to keep track of level
        def dfs(node, level):
            if node is None:
                return
            # if not none, means theres a node there
            # if node is at level and len(res) = level, res has level - 1 lists and thus needs one more for new level
            if len(res) == level:
                # adding [] to list
                res.append([])
            # at level, adds node
            res[level].append(node.val)
            # calls on left and right with next level
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        # calls with root level 0
        dfs(root, 0)
        return res