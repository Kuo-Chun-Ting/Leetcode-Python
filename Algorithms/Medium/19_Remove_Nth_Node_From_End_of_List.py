from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent.absolute()))
from models.list_node import ListNode
from tool.linked_list_operation import array_to_list_node, travel_node

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # count the length of the node
        length = 0
        curr = head
        while curr != None:
            length += 1
            curr = curr.next
            
        index = length - n
        if index < 0 or index >= length:
            return
        
        # find the n-th node 
        last = None
        curr = head
        for i in range(length-n):
            last = curr
            curr = curr.next
        
        # remove the n-th node from the end
        if last is None: # curr is at the beginning
            head = curr.next
            curr.next = None
            curr = None
        elif curr.next is None: # curr is at the end
            last.next = None
        else:
            last.next = curr.next
            curr.next = None
        return head
        
s = Solution()
node = array_to_list_node([0,1,2,3,4,5,6])
print('before')
travel_node(node)
node = s.removeNthFromEnd(node, 0)
print('after')
travel_node(node)
