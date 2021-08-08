class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None       
    
    def print_all(self):
        curr = self
        while curr != None:
            print(curr.val)
            curr = curr.next
    
    def add(self, val: int):
        curr = self
        while curr.next != None:
            curr = curr.next
        curr.next = ListNode(val)
    
def arr_to_node(arr:[]) -> ListNode:
    if arr is None or len(arr) == 0:
        return None
    
    head = ListNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
        # 不要使用ListNode.add效能比較好
        # 因為add每次要從頭找最後一個node
        curr.next = ListNode(arr[i])
        curr = curr.next
    return head

