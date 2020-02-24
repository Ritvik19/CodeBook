class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.data}"


count = 0


def kthSmallestInBST(root, k):
    global count
    if root is None:
        return None
    left = kthSmallestInBST(root.left, k)
    if left:
        return left
    count += 1
    if(count == k):
        return root
    return kthSmallestInBST(root.right, k)


def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.data:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node


def inorderTraversal(node):
    res = []
    if node:
        res = inorderTraversal(node.left)
        res.append(node.data)
        res = res + inorderTraversal(node.right)
    return res


if __name__ == "__main__":
    root = Node(10)
    root = insert(root, 50)
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 70)
    root = insert(root, 60)
    root = insert(root, 80)
    print(*inorderTraversal(root))
    print(f"3th Smallest: {kthSmallestInBST(root, 3)}")
