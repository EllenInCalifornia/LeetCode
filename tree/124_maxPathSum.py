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
        each_node_max = set()
        # memo records one branch max of each value
        memo = {}
        with_cur = self.with_curr(root, memo, each_node_max)
        res1 = max(memo.values())
        res2 = max(each_node_max)
        return max(res1, res2)

    def with_curr(self, node, memo, each_node_max):

        if not node:
            return float("-inf")
        if node in memo:
            return memo[node]
        right_max = self.with_curr(node.right, memo, each_node_max)
        memo[node.right] = right_max
        left_max = self.with_curr(node.left, memo, each_node_max)
        memo[node.left] = left_max
        one_branch_max = max(node.val, node.val + right_max, node.val + left_max)
        memo[node] = one_branch_max
        node_max = max(one_branch_max, node.val + right_max + left_max)
        each_node_max.add(node_max)  
        return memo[node]
      