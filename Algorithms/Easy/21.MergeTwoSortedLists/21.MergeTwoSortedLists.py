class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        last = l1
        while last is not None and last.next != None:
            last = last.next
        if last is not None:
            last.next = l2
        else:
            l1 = l2
        
        data =[]
        curr = l1
        while curr != None:
            data.append(curr.val)
            curr = curr.next
        print(data)
        print()
        
        self.quick＿sort(data, 0, len(data) - 1)
        print(data)
        
        if len(data) > 0:
            node = ListNode(data[0])
            point = node
            for i in range(1, len(data)):
                point.next = ListNode(data[i])
                point = point.next
            return node
        else:
            return None
        
    def quick＿sort(self, data, left, right): # 輸入資料，和從兩邊開始的位置
        if left >= right :            # 如果左邊大於右邊，就跳出function
            return

        i = left                      # 左邊的代理人
        j = right                     # 右邊的代理人
        key = data[left]                 # 基準點

        while i != j:                  
            while data[j] > key and i < j:   # 從右邊開始找，找比基準點小的值
                j -= 1
            while data[i] <= key and i < j:  # 從左邊開始找，找比基準點大的值
                i += 1
            if i < j:                        # 當左右代理人沒有相遇時，互換值
                data[i], data[j] = data[j], data[i] 

        # 將基準點歸換至代理人相遇點
        data[left] = data[i] 
        data[i] = key

        self.quick_sort(data, left, i-1)   # 繼續處理較小部分的子循環
        self.quick_sort(data, i+1, right)  # 繼續處理較大部分的子循環
                
l1 = ListNode(3)
l1.next = ListNode(2)
l1.next.next = ListNode(1)

l2 = ListNode(4)
l2.next = ListNode(2)
l2.next.next = ListNode(2)
s = Solution()
s.mergeTwoLists(None, ListNode(0))
print()