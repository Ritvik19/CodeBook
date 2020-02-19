class Node: 
    def __init__(self, data): 
        self.data = data
        self.next = None 

    def __str__(self):
        return str(self.data)
    
class CircularLinkedList: 
    def __init__(self):  
        self.head = None
        self.tail = None

    def length(self):
        count = 0
        if self.head is not None:
            current = self.head
            while True:
                current = current.next
                count += 1
                if (current == self.head):
                        break
        return count

    def traverse(self):
        if self.head is not None:
            current = self.head
            while True:
                print(current.data, end=" -> ")
                current = current.next
                if (current == self.head):
                        break
            print('end')

    def insertAtBeginning(self, data):        
        newnode = Node(data)
        if self.length() == 0:
            self.head = newnode
            self.tail = self.head
        else:
            newnode.next = self.head
            self.head = newnode
        self.tail.next = self.head

    def insertAtEnd(self, data):
        newnode = Node(data)
        if self.length() == 0:
            self.head = newnode
            self.tail = self.head
        else:
            self.tail.next = newnode
            self.tail = newnode
        self.tail.next = self.head

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
            self.tail.next = self.head

    def deleteFromEnd(self):
        if self.length() == 0:
            print("The list is empty")
        else:
            currentnode = self.head
            previousnode = self. head
            while currentnode is not self.tail:
                previousnode = currentnode
                currentnode = currentnode.next
            previousnode.next = self.head
            self.tail = previousnode

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

if __name__ == '__main__':
    linkedlist = CircularLinkedList()
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
