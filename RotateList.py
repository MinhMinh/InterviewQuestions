# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        n = 0
        current = head
        while (current is not None):
            current = current.next
            n += 1
        
        if n < 2: return head
            
        k = k % n            
        if k == 0 or head is None: return head
        
        previous = head
        current = head
        for i in range(k):
            current = current.next
            if current is None: return head
            
        while current.next is not None:
            current = current.next
            previous = previous.next
        
        newHead = previous.next
        previous.next = None
        current.next = head
        
        return newHead
        
        
def printList(node):
    while node is not None:
        print node.val,
        node = node.next
    print     
    
r = Solution()

nodes = []
for i in range(6):
    nodes.append(ListNode(i))

print 

for i in range(5):
    nodes[i].next = nodes[i + 1]    
    
printList(nodes[0])

head = r.rotateRight(nodes[0], 7)
printList(head)

