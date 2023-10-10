class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def symmetricalTree(tree):
    return trees_are_mirrored(tree.left, tree.right)
    
def trees_are_mirrored(left, right):
    if left is not None and right is not None and left.value == right.value:
        return trees_are_mirrored(left.left, right.right) and trees_are_mirrored(left.right, right.left)
    return left == right