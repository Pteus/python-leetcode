# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        curr_sum = 0

        return self.dfs(root, curr_sum, targetSum)

    def dfs(self, node, curr_sum, targetSum):
        if not node:
            return False

        curr_sum += node.val

        if not node.left and not node.right:
            return curr_sum == targetSum

        if self.dfs(node.left, curr_sum, targetSum):
            return True
        if self.dfs(node.right, curr_sum, targetSum):
            return True

        curr_sum -= node.val
        return False
