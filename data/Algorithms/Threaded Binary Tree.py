class Node():
    def __init__(self, key):
        self.left = self.right = None
        self.key = key
        self.isThreaded = None

def createThreaded(root):
    if root == None:
        return None
    if root.left == None and root.right == None:
        return root
    if root.left != None:
        l = createThreaded(root.left)
        l.right = root
        l.isThreaded = True
    if root.right == None:
        return root
    return createThreaded(root.right)

def leftMost(root):
    while root != None and root.left != None:
        root = root.left
    return root

def inOrder(root):
    if root == None:
        return
    cur = leftMost(root)

    while cur != None:
        print(cur.key, end=" ")
        if cur.isThreaded:
            cur = cur.right
        else: 
            cur = leftMost(cur.right)

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    createThreaded(root)
    print("Inorder traversal of created threaded tree is")
    inOrder(root)
