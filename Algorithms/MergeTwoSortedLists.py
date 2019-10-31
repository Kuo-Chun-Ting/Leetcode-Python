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
        print()
        
        self.quick＿sort(data, 0, len(data) - 1)
        
    def quick＿sort(self, data: [], i: int, j: int):
        if i == j:
            return data
        pivot = data[i]
        i += 1
        while True:
            while data[i] <= pivot and i< j:
                i += 1
            while data[j] >= pivot and j > 1:
                j -= 1
            if i < j:
                self.swap(data, i, j)
                print()
            elif i == j:
                pass
            else:
                self.swap(data, 0, j)
                break
        self.quick＿sort(data, 0, j-1)
        self.quick＿sort(data, j+1, len(data)-1)
                
    def swap(self, data: [], i: int, j: int):
        temp = data[i]
        data[i] = data[j]
        data[j] = temp
        print(data)
        
l1 = ListNode(3)
l1.next = ListNode(2)
l1.next.next = ListNode(1)

l2 = ListNode(4)
l2.next = ListNode(2)
l2.next.next = ListNode(2)
s = Solution()
s.mergeTwoLists(l1, l2)
print()