class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def length(head):
    node = head
    count = 0
    while node is not None:
        node = node.next
        count += 1
    return count


def removeKthNodeFromEnd(head, k):
    pos = length(head) - k + 1
    if pos == 1:
        head.value = head.next.value
        head.next = head.next.next
        return

    node = head
    prev = None
    for i in range(pos - 1):
        prev = node
        node = node.next

    prev.next = node.next
    node.next = None
    

    
