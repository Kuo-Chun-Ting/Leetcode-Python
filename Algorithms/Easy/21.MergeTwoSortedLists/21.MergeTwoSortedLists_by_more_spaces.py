class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is not None and l2 is not None:
            curr_l1 = l1 
            curr_l2 = l2
            last_l2 = None
            while curr_l1 is not None:
                new_node = None
                while curr_l2 is not None:
                    if curr_l1.val <= curr_l2.val:
                        new_node = ListNode(curr_l1.val)
                        new_node.next = curr_l2
                        if last_l2 is None: 
                            l2 = new_node
                        else:
                            last_l2.next = new_node
                        break
                    last_l2 = curr_l2
                    curr_l2 = curr_l2.next
                    
                if new_node is None:
                    new_node = ListNode(curr_l1.val)
                    last_l2.next = new_node
                    last_l2 = None
                    curr_l2 = l2
                else:
                    last_l2 = new_node
                    curr_l2 = new_node.next
                curr_l1 = curr_l1.next
            return l2
        elif l1 is None and l2 is None:
            return None
        elif l1 is not None:
            return l1
        else:
            return l2
        
def create_node(data: []) -> ListNode:
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
    
l1 = create_node([-10,-10,-9,-4,1,6,6])
l2 = create_node([-7])
s = Solution()
s.mergeTwoLists(l1, l2)