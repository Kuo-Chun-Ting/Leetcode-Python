from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent.absolute()))
from models.list_node import ListNode
        
class LinkedListOperation:
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
    
def array_to_list_node(data:[]):
    if data is None or len(data) == 0:
        return None
    
    node = ListNode(data[0])
    curr = node    
    for i in range(1, len(data)):
        curr.next = ListNode(data[i])
        curr = curr.next
    return node

def travel_node(node: ListNode):
        if node is None:
            print('node is None')
        else:
            curr = node
            while curr is not None:
                print(curr.val)
                curr = curr.next
        
    
    
# l = LinkedListOperation()
# l.insert_at_beginning(99)
# l.insert_at_beginning(30)
# l.insert_at_beginning(19)
# l.insert_at_end(50)
# l.insert_at_end(28)
# l.travel_node()

node = array_to_list_node([1,2,3])
node1 = array_to_list_node(None)

travel_node(node)
travel_node(node1)