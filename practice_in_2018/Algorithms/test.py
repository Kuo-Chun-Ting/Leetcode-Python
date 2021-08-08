from models.binary_tree import TreeNode, arr_to_node

arr = [3,9,20,None,None,15,7] 
n = len(arr) 
root = None
root = arr_to_node(arr, root, 0, n) 
print('in order')
# root.in_order()
print('level order')
root.level_order(root)