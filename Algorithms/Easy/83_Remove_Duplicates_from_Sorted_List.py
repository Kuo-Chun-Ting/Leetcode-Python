from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent.absolute()))
print(sys.path)
from models.list_node import ListNode, arr_to_node

class Solution(object):
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head
        while curr != None:
            if curr.next != None and curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
                
node = arr_to_node([1,1,2,3,4,4,5])
s = Solution()
new = s.deleteDuplicates(node)
new.print_all()
        