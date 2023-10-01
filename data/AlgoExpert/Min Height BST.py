def minHeightBst(array):
    return construct_min_height_BST(array, 0, len(array)-1)

def construct_min_height_BST(array, beg_idx, end_idx):
    if end_idx < beg_idx:
        return None
    mid_idx = (beg_idx + end_idx) // 2
    bst = BST(array[mid_idx])
    bst.left = construct_min_height_BST(array, beg_idx, mid_idx - 1)
    bst.right = construct_min_height_BST(array, mid_idx + 1, end_idx)
    return bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
