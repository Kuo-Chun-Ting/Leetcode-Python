from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent.absolute()))
from models.binary_tree import TreeNode, arr_to_node

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.is_mirror(root, root)
    
    def is_mirror(self, t1:TreeNode, t2:TreeNode) -> bool:
        if t1 == None and t2 == None:
            return True
        if t1 == None or t2 == None:
            return False
        return t1.val == t2.val and self.is_mirror(t1.right,t2.left) and self.is_mirror(t1.left,t2.right)

s = Solution()
node = None
arr = [1,2,2,3,4,4,3]
node = arr_to_node(arr,node, 0, len(arr))
node.level_order(node)
result = s.isSymmetric(node)
print(result)
