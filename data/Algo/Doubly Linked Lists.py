class Node: 
    def __init__(self, data): 
        self.data = data
        self.next = None
        self.prev = None

class LinkedList: 
    def __init__(self):  
        self.head = None
        self.tail = None

    def length(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def traverse(self):
        current = self.head
        print('head', end=" <-> ")
        while current is not None:
            print(current.data, end=" <-> ")
            current = current.next
        print('tail')

    def reverse(self):
        current = self.tail
        print('tail', end=" <-> ")
        while current is not None:
            print(current.data, end=" <-> ")
            current = current.prev
        print('head')
        
    def insertAtBeginning(self, data):
        newnode = Node(data)
        if self.length() == 0:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode

    def insertAtEnd(self, data):
        newnode = Node(data)
        if self.length() == 0:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode

    def insertAtPos(self, pos, data):
        if pos > self.length() or pos < 0:
            print("invalid Position")
        else:
            if pos == 0:
                self.insertAtBeg(data)
            elif pos == self.length():
                self. insert.AtEnd(data)
            else:
                newnode = Node(data)
                count = 0
                current = self.head
                while count < pos-1:
                    count += 1
                    current = current.next
                newnode.next = current.next
                newnode.prev = current
                current.next.prev = newnode
                current.next = newnode

    def deleteFromBeginning(self):
        if self.length() == 0:
            print("The list is empty")
        else:
            self.head = self.head.next
            self.head.prev = None

    def deleteFromEnd(self):
        if self.length() == 0:
            print("The list is empty")
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def deleteAtPos(self, pos):
        count = 0
        currentnode = self.head
        previousnode = self. head
        if pos > self.length() or pos < 0:
            print("invalid Position")
        else:
            if pos == 0:
                self.deleteFromBeginning()
            elif pos == self.length():
                self.deleteFromEnd()
            else:
                while currentnode.next is not None or count < pos:
                    count += 1
                    if count == pos:
                        previousnode.next = currentnode.next
                        currentnode.next.prev = previousnode
                        return
                    else:
                        previousnode = currentnode
                        currentnode = currentnode.next

    def clear(self):
        self.head = None

if __name__ == '__main__':
    linkedlist = LinkedList()
    linkedlist.insertAtBeginning(3)
    linkedlist.insertAtBeginning(2)
    linkedlist.insertAtBeginning(1)
    linkedlist.insertAtEnd(5)
    linkedlist.insertAtEnd(6)
    linkedlist.insertAtPos(3, 4)
    linkedlist.deleteFromBeginning()
    linkedlist.deleteFromEnd()
    linkedlist.deleteAtPos(3)
    print(f"Length: {linkedlist.length()}")
    linkedlist.traverse()
    linkedlist.reverse()
