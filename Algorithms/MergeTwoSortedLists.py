class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        last = l1
        while last.next != None:
            last = last.next
        last.next = l2
        print('finished')

l1 = ListNode(3)
l1.next = ListNode(2)
l1.next.next = ListNode(1)

l2 = ListNode(4)
l2.next = ListNode(2)
l2.next.next = ListNode(2)
s = Solution()
s.mergeTwoLists(l1, l2)