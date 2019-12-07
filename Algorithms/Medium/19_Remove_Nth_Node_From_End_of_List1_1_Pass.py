from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent.absolute()))
from models.list_node import ListNode
from tool.linked_list_operation import array_to_list_node, travel_node

# one pass solution
# Maintain two nodes and make them keep n gaps so that the position of the 
# second node will be the right position to be removed when the first node get the end
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first = head
        second = head
        first_last = None
        second_last = None
        
        gap = 0
        while first.next != None:
            first_last = first
            first = first.next
            if gap == n:
                second_last = second
                second = second.next
            if gap < n:
                gap += 1
                
        if n == 0:
            return
        elif n <= gap:
            self.remove_node(head, second, second.next)    
        else:
            head = second.next
            second.next = None
            second = None
        return head
    
    # remove node
    def remove_node(self, head, last, curr):
            if last is None: # curr is at the beginning
                head = curr.next
                curr.next = None
                curr = None
            elif curr.next is None: # curr is at the end
                last.next = None
            else:
                last.next = curr.next
                curr.next = None
            
s = Solution()
node = array_to_list_node([0,1,2,3,4,5,6])
print('before')
travel_node(node)
node = s.removeNthFromEnd(node, 1)
print('after')
travel_node(node)
