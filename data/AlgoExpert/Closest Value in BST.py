# O (log n) O(1)

def findClosestValueInBst(tree, target):
    current = tree
    closest = current.value
    while current is not None:
        if abs(target - closest) > abs(target - current.value):
            closest = current.value
        if target < current.value:
            current = current.left
        elif target > current.value:
            current = current.right
        else:
            break
    return closest

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None