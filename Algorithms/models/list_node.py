class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None       
    
    def print_all(self):
        curr = self
        while curr != None:
            print(curr.val)
            curr = curr.next
            
def arr_to_node(arr:[]) -> ListNode:
    if arr is None or len(arr) == 0:
        return None
    
    head = ListNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next
    return head

node = arr_to_node([1,2,3])
node.print_all()
