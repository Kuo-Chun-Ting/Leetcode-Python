from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        res = ListNode(0)
        carry = 0
        current = None

        while l1 is not None or l2 is not None or carry != 0:
            if current is None:
                current = res
            else:
                current.next = ListNode(0)
                current = current.next

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            current.val = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return res
