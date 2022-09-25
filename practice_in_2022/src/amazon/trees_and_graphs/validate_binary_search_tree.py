import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BFSSolution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, min_val=-math.inf, max_val=math.inf):
            if not node:
                return True

            if node.val <= min_val or node.val >= max_val:
                return False

            return validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)

        return validate(root)


class DFSSolution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = [(root, -math.inf, math.inf)]
        while len(stack) != 0:
            item = stack.pop()
            node = item[0]
            if node is None:
                continue

            min_val = item[1]
            max_val = item[2]
            if node.val <= min_val or node.val >= max_val:
                return False

            stack.append((node.left, min_val, node.val))
            stack.append((node.right, node.val, max_val))

        return True


if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(BFSSolution().isValidBST(root))
    print(DFSSolution().isValidBST(root))
