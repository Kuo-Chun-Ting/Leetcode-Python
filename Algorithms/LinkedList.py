class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def travel_node(self):
        if self.head is None:
            print('no data')
        else:
            curr = self.head
            while curr is not None:
                print(curr.val)
                curr = curr.next
            
    def insert_at_beginning(self, data):
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node
        
    def insert_at_end(self, data):
        new_node = ListNode(data)
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node
    
l = LinkedList()
l.insert_at_beginning(99)
l.insert_at_beginning(30)
l.insert_at_beginning(19)
l.insert_at_end(50)
l.insert_at_end(28)
l.travel_node()