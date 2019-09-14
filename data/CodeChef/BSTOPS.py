class Node:
    def __init__(self, key, pos):
        self.key = key
        self.left = None
        self.right = None
        self.pos = pos

def insert(node, key, pos):
    if node is None:
        print (pos)
        return Node(key, pos)
    if key < node.key:
        node.left = insert(node.left, key, 2 * pos)
    else:
        node.right = insert(node.right, key, 2 * pos + 1)
    return node


def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def deleteNode(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif key > root.key:
        root.right = deleteNode(root.right, key)
    else:
        print (root.pos)
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)
    return root


root = None
cases = None
try:
    inp = ''
    x = []
    pos = -1
    for i in range(int(input())):
        inp = input()
        x = inp.split(' ')
        if x[0] == 'i':
            root = insert(root, int(x[1]), 1)
        elif x[0] == 'd':
            root = deleteNode(root, int(x[1]))
except:
    pass
