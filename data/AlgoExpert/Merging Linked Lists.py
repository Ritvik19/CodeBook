class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergingLinkedLists(linkedListOne, linkedListTwo):
    node_one = linkedListOne
    node_two = linkedListTwo
    count_one = 0
    count_two = 0
    while node_one is not None:
        count_one += 1
        node_one = node_one.next

    while node_two is not None:
        count_two += 1
        node_two = node_two.next

    long_node = linkedListOne if count_one > count_two else linkedListTwo
    short_node = linkedListTwo if count_one > count_two else linkedListOne

    for _ in range(abs(count_two - count_one)):
        long_node = long_node.next

    while long_node is not short_node:
        long_node = long_node.next
        short_node = short_node.next

    return short_node
