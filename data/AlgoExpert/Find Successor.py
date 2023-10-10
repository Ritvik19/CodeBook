# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def inorder(node, order=[]):
    if node is None:
        return order
    inorder(node.left, order)
    order.append(node)
    inorder(node.right, order)

    return order

def findSuccessor(tree, node):
    inorder_traversal = inorder(tree)

    idx = inorder_traversal.index(node)
    if idx == len(inorder_traversal) - 1:
        return None

    return inorder_traversal[idx + 1]
    return None
