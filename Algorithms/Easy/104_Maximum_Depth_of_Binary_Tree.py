from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent.absolute()))
from models.binary_tree import TreeNode, arr_to_node

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
    
s = Solution()
arr = [3,9,20,None,None,15,7]
node = arr_to_node(arr,None, 0, len(arr))
print(s.maxDepth(node))