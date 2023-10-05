class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    sum_head = LinkedList(0)
    current = sum_head
    carry = 0

    node_one = linkedListOne
    node_two = linkedListTwo
    while node_one is not None or node_two is not None or carry != 0:
        val_one = node_one.value if node_one is not None else 0
        val_two = node_two.value if node_two is not None else 0
        sum_val = val_one + val_two + carry
        new_val = sum_val % 10
        carry = sum_val // 10

        current.next = LinkedList(new_val)
        current = current.next

        node_one = node_one.next if node_one is not None else None
        node_two = node_two.next if node_two is not None else None
    
    return sum_head.next
