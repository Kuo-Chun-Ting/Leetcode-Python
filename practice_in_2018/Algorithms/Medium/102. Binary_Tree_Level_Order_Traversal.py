from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent.absolute()))
from models.binary_tree import TreeNode, arr_to_node, arr_to_treenode
from typing import List

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.dfs(root, 0, res)
        return res
        
    def dfs(self, root: TreeNode, depth: int, res: []):
        if root == None:
            return
        if len(res) < depth + 1:
            res.append([])
        res[depth].append(root.val)
        
        self.dfs(root.left, depth+1, res)
        self.dfs(root.right, depth+1, res)

node = arr_to_treenode([1,2,3,4,5])
s = Solution()
retsult = s.levelOrder(node)
print(retsult)           
        

