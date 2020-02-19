class Stack():
    def __init__(self, size):
        self.size = size
        self.stack = []
        self.tos = -1

    def isEmpty(self):
        return self.tos == -1

    def isFull(self):
        return self.tos == self.size-1

    def push(self, data):
        if self.isFull():
            print("Stack Overflow")
        else:
            self.tos += 1
            self.stack.append(data)
            print("Added", data)

    def pop_(self):
        if self.isEmpty():
            print("Stack Underflow")
        else:
            element = self.stack.pop(self.tos)
            self.tos -= 1
            return element

    def top(self):
        if self.isEmpty():
            print("Stack Underflow")
        else:
            return self.stack[-1]

    def display(self):
        print("Stack:")
        for elem in self.stack[::-1]:
            print("\t", elem)

    def clear(self)            :
        self.tos = -1
        self.stack = []


if __name__ == "__main__":
    n = 2
    stack = Stack(n)
    print("Stack Created of size", n)
    print("POP called:", end="\n\t")
    stack.pop_()
    stack.push(5)
    stack.push(4)
    print("PUSH called again:", end="\n\t")
    stack.push(3)
    stack.display()
    print('TOP: ', stack.top())
    print('TOS: ', stack.tos)
    print('POP: ', stack.pop_())
    print('TOS: ', stack.tos)
    stack.display()
