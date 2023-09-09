# O(n) O(1)

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    current_node = linkedList
    while current_node is not None:
        next_node = current_node.next
        while next_node is not None and current_node.value == next_node.value:
            next_node = next_node.next

        current_node.next = next_node
        current_node = next_node

    return linkedList