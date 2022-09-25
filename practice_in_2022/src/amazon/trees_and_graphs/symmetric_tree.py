from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.is_mirror(root, root)

    def is_mirror(self, t1: TreeNode, t2: TreeNode) -> bool:
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False

        return (
            t1.val == t2.val
            and self.is_mirror(t1.left, t2.right)
            and self.is_mirror(t1.right, t2.left)
        )
