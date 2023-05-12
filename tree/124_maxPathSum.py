# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            # [-3], error
            return float("-inf") 
        right_max = self.maxPathSum(root.right)
        left_max = self.maxPathSum(root.left)
        return max(root.val, root.val + right_max, root.val + left_max, right_max, left_max, root.val + right_max + left_max)