from queue import Queue
from typing import Optional
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class RecursionSolution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if root is None:
            return levels

        def helper(node: TreeNode, level: int):
            if len(levels) == level:
                levels.append([])

            levels[level].append(node.val)
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        return levels


class IterationSolution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if root is None:
            return levels

        queue = Queue()
        queue.put(root)
        level = 0
        while queue.qsize() > 0:
            levels.append([])
            level_len = queue.qsize()

            for i in range(level_len):
                node = queue.get()
                levels[level].append(node.val)

                if node.left:
                    queue.put(node.left)
                if node.right:
                    queue.put(node.right)

            level += 1
        return levels
    
    
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    print(IterationSolution().levelOrder(root))
    