from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent.absolute()))
from models.list_node import ListNode

class DSFactory:
    def array_to_listnode(self, data: []) -> ListNode:
        length = len(data)
        if length == 0:
            return None
        head = None
        curr = None
        for i in range(length):
            if i == 0:
                curr = ListNode(data[i])
                head = curr
            else:
                curr.next = ListNode(data[i])
                curr = curr.next
        return head

factory = DSFactory()
node = factory.array_to_listnode([1,2,3])