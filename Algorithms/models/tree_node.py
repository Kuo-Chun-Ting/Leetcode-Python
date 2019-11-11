class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
    def print_node(self):
        if self.left:
            self.left.print_node()
        print(self.val)
        if self.right:
            self.right.print_node()
        
    def insert(self, data):
    # Compare the new value with the parent node
        if self.val:
            if data < self.val:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            elif data > self.val:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
            
def array_to_tree_node(arr, root, i, n): 
    # Base case for recursion  
    if i < n: 
        temp = TreeNode(arr[i])  
        root = temp  
  
        # insert left child  
        root.left = array_to_tree_node(arr, root.left, 2 * i + 1, n)  
  
        # insert right child  
        root.right = array_to_tree_node(arr, root.right, 2 * i + 2, n) 
    return root 
        
arr = [1, 2, 3, 4, 5, 6, 6, 6, 6] 
n = len(arr) 
root = None
root = array_to_tree_node(arr, root, 0, n) 
root.print_node()

node = TreeNode(1)
node.insert(9)
node.insert(8)
node.insert(8)
node.insert(8)
node.insert(2)
node.insert(1)
node.print_node()
        