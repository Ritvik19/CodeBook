class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def reverse_inorder_traverse(node, k, temp):
    if node is None or temp['visited'] >= k:
        return 

    reverse_inorder_traverse(node.right, k, temp)
    if temp['visited'] < k:
        temp['visited'] += 1
        temp['value'] = node.value
        reverse_inorder_traverse(node.left, k, temp)



def findKthLargestValueInBst(tree, k):
    temp = {'visited': 0, 'value': -1}
    reverse_inorder_traverse(tree, k, temp)
    return temp['value']
