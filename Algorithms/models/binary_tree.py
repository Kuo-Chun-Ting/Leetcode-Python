class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
    def in_order(self):
        if self.left:
            self.left.in_order()
        print(self.val)
        if self.right:
            self.right.in_order()
            
    def level_order(self,root):
        res = []
        self.dfs(root, 0, res)
        for item in res:
            print(item)
        return res
    
    def dfs(self, root, depth, res):
        if root == None:
            return res
        if len(res) < depth+1:
            res.append([])
        res[depth].append(root.val)
        self.dfs(root.left, depth+1, res)
        self.dfs(root.right, depth+1, res)
        

def arr_to_node(arr, root, i, n): 
    if i < n: 
        root = TreeNode(arr[i])  
        root.left = arr_to_node(arr, root.left, 2 * i + 1, n)  
        root.right = arr_to_node(arr, root.right, 2 * i + 2, n) 
    return root 
