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
        
        gap = 1
        while first.next != None:
            first_last = first
            first = first.next
            if gap == n:
                second_last = second
                second = second.next
            if gap < n:
                gap += 1
                
        if gap == n:
            # normal confition
            if second_last is None: # curr is at the beginning
                head = second.next
                second.next = None
                second = None
            elif second.next is None: # Purr is at the end
                second_last.next = None
            else:
                second_last.next = second.next # curr is at the end
                second.next = None
        elif gap < n:
            # n is out of the length of ListNode
            head = second.next
            second.next = None
            second = None
        else:
            # n is less then 0
            return
        return head
            
s = Solution()
node = array_to_list_node([0,1,2,3,4,5,6])
print('before')
travel_node(node)
node = s.removeNthFromEnd(node, -2)
print('after')
travel_node(node)
