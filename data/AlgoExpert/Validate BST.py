class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree, min_val=float("-inf"), max_val=float("inf")):
    if tree is None:
        return True
    if tree.value < min_val or tree.value >= max_val:
        return False
    left_is_valid = validateBst(tree.left, min_val, tree.value)
    right_is_valid = validateBst(tree.right, tree.value, max_val)
    return left_is_valid and right_is_valid
    
