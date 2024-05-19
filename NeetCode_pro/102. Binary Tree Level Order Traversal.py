# Definition for a binary tree node.
from typing import Deque, List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = Deque()

        if root:
            q.append(root)

        while len(q) > 0:
            vals = []
            for i in range(len(q)):
                curr = q.popleft()
                vals.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(vals)

        return res
