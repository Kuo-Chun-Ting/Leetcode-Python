from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prehead = ListNode(-1)
        current = prehead
        
        while list1 and list2:
            current.next = ListNode(0)
            current = current.next
            
            if list1.val < list2.val:
                current.val = list1.val
                list1 = list1.next
            else:
                current.val = list2.val
                list2 = list2.next
            
        current.next = list1 if list1 else list2
        return prehead.next