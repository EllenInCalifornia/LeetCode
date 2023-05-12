
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        split = []
        def dfs(root):
            if not root:
                return 0
            # one_branch max, can choose to add or not add 
            leftmax = max(0, dfs(root.left))
            rightmax = max(0, dfs(root.right))
            
            # return one_branch max 
            
            # compute split
            split.append(root.val + leftmax + rightmax)
            return max(root.val + leftmax, root.val + rightmax)
        dfs(root)
        return max(split)



      