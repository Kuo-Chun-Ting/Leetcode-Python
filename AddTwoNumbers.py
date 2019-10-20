# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        x = self.getValue(l1)
        print(x.val)
    
    def getValue(self, l):
        if l.next != None:
            self.getValue(l.next)
        else:
            return l
        
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l1 = ListNode(5)
l1.next = ListNode(6)
l1.next.next = ListNode(4)

s = Solution()
s.addTwoNumbers(l1,l1)