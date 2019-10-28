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
        
        data =[]
        curr = l1
        while curr != None:
            data.append(curr.val)
            curr = curr.next
        print(data)
        
        self.quickSort(data)
        
    def quickSort(self, data: []):
        pivot = data[0]
        i = 1
        j = len(data) - 1
        left = None
        right = None
        while True:
            
            if left is None:
                if data[i] < pivot:
                    i += 1
                else:
                    left = data[i]
                    
            if right is None:
                if data[j] > pivot:
                    j -= 1
                else:
                    right = data[j]
                    
            if left is not None and right is not None:
                data[i] = right
                data[j] = left
                print(data)
                i = 1
                j = j = len(data) - 1
                left = None
                right = None

            if i >= j:
                data[0] = right
                data[j] = pivot
                print(data)
                break
        
l1 = ListNode(3)
l1.next = ListNode(2)
l1.next.next = ListNode(1)

l2 = ListNode(4)
l2.next = ListNode(2)
l2.next.next = ListNode(2)
s = Solution()
s.mergeTwoLists(l1, l2)