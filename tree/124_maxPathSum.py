# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 含有current node的最大值
        # without current node
        memo = {}
        with_cur = self.with_curr(root, memo)
        return max(memo.values())

    def with_curr(self, root, memo):

        if not node:
            return float("-inf")
        if node in memo:
            return memo[node]
        right_max = self.with_curr(node.right)
        memo[node.right] = right_max
        left_max = self.with_curr(node.left)
        memo[node.left] = left_max
        memo[node] = max(node.val, node.val + right_max, node.val + left.max, node.val + right_max + left_max)
        return memo[node]
        # [1,-2,-3,1,3,-2,null,-1] 
      