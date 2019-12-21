from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent.absolute()))
from models.list_node import ListNode, arr_to_node

def swapNode(head: ListNode):
    node.print_all()
    


class Solution:
    def swapPairs(self, head: ListNode) ->ListNode:
        if head is not None:
            pre = head
            curr = head
            next = curr.next
            
            while curr is not None and curr.next is not None:
                # swap node
                curr.next = next.next
                next.next = curr
                
                if curr == head:
                    pre = next
                    head = pre
                else:
                    pre.next = next
                    pre = pre.next
                
                # move to next node
                pre = curr
                curr = curr.next
                if curr is not None:
                    next = curr.next
            head.print_all()
            return head
        
node = arr_to_node([1,2,3,4,5,6])
s = Solution()
s.swapPairs(node)

