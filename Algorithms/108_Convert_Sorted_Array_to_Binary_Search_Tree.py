from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent.absolute()))
from models.binary_tree import TreeNode, arr_to_node
from typing import List

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        length = len(nums)
        
        if length == 0:
            return None
        if length == 1:
            return TreeNode(nums[0])
        
        index = length//2
        root = TreeNode(nums[index])
        root.left = self.sortedArrayToBST(nums[0:index])
        root.right = self.sortedArrayToBST(nums[index+1:length])
        return root

s = Solution()
arr = [-10,-3,0,5,9]
node = s.sortedArrayToBST(arr)
node.level_order(node)