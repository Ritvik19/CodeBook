""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""


def check_binary_search_tree_(root):
    return check_node(root, -1, 10001)


def check_node(node, Min, Max):
    if not node:
        return True
    if Min < node.data < Max:
        return check_node(node.left, Min, node.data) and check_node(node.right, node.data, Max)
    return False
