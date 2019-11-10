from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent.absolute()))
print(sys.path)
from LinkedList.ListNode import ListNode

class Solution(object):
    def addTwoNumbers(self, l1:ListNode, l2:ListNode) -> ListNode :
        curr1 = l1
        curr2 = l2
        carry = 0
        total = None
        current = None
        
        while curr1 != None or curr2 != None:
            sum = 0
            sum += carry if carry != 0 else 0
            sum += curr1.val if curr1 != None else 0
            sum += curr2.val if curr2 != None else 0       
            
            if sum >= 10:
                sum -= 10
                carry = 1
            else:
                carry = 0
            
            if total == None:
                total = ListNode(sum)
                current = total
            else:
                current.next = ListNode(sum)
                current = current.next
                
            curr1 = curr1.next if curr1 != None else None
            curr2 = curr2.next if curr2 != None else None
        
        if carry > 0:
            current.next = ListNode(carry)
        return total   
    
    
l1 = ListNode(1)
l2 = ListNode(9)
l2.next = ListNode(9)

s = Solution()
total = s.addTwoNumbers(l1,l2)