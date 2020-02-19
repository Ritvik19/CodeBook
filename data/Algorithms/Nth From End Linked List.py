class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __str__(self):
        return str(self.data)

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def length(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print('end')

    def insertAtBeginning(self, data):
        newnode = Node(data)
        if self.length() == 0:
            self.head = newnode
        else:
            newnode.next = self. head
            self.head = newnode

    def insertAtEnd(self, data):
        newnode = Node(data)
        if self.length() == 0:
            self.head = newnode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newnode

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
                current.next = newnode

    def deleteFromBeginning(self):
        if self.length() == 0:
            print("The list is empty")
        else:
            self.head = self.head.next

    def deleteFromEnd(self):
        if self.length() == 0:
            print("The list is empty")
        else:
            currentnode = self.head
            previousnode = self. head
            while currentnode.next is not None:
                previousnode = currentnode
                currentnode = currentnode.next
            previousnode.next = None

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
                        return
                    else:
                        previousnode = currentnode
                        currentnode = currentnode.next

    def clear(self):
        self.head = None

    def nthFromEnd(self, n):
        if n < 0:
            return None
        current = self.head
        count = 0
        while count < n and current is not None:
            current = current.next
            count += 1
        nth = self.head
        while current.next is not None:
            current = current.next
            nth = nth.next
        return nth

if __name__ == '__main__':
    linkedlist = SinglyLinkedList()
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
    n = 1
    print(f"{n}th from end: {linkedlist.nthFromEnd(n)}")
