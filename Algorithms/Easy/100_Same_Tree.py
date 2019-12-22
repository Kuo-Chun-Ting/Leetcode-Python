from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent.absolute()))
from models.binary_tree import TreeNode, arr_to_node

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        while p != None or q != None:
            if p == None or q == None or (p.val != q.val):
                return False
            else:
                 if not self.isSameTree(p.left, q.left):
                     return False
                 if not self.isSameTree(p.right, q.right):
                     return False
                 return True
        return True

s = Solution()
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
q = TreeNode(1)
q.left = TreeNode(2)

result = s.isSameTree(p, q)
print(result)