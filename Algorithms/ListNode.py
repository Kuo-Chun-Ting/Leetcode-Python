class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class NodeFactory:       
    def create_node(self, data: []) -> ListNode:
        length = len(data)
        if length == 0:
            return None
        head = None
        curr = None
        for i in range(length):
            if i == 0:
                curr = ListNode(data[i])
                head = curr
            else:
                curr.next = ListNode(data[i])
                curr = curr.next
        return head

node = NodeFactory().create_node([1,2,3])