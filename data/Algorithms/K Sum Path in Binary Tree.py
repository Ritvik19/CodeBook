from BinaryTree import Node


def printKPathUtil(root, path, k):
    if root is None:
        return
    path.append(root.data)
    printKPathUtil(root.left, path, k)
    printKPathUtil(root.right, path, k)
    f = 0
    for j in range(len(path) - 1, -1, -1):
        f += path[j]
        if (f == k):
            print(*path[j:])

    path.pop(-1)

def printKPath(root, k):
    path = []
    printKPathUtil(root, path, k)

if __name__ == "__main__":
    root = Node(27)
    root.left = Node(14)
    root.right = Node(35)
    root.left.left = Node(10)
    root.left.right = Node(19)
    root.right.left = Node(31)
    root.right.right = Node(42)
    root.left.left.left = Node(45)
    print("Inorder:")
    print(*root.inorderTraversal(root))
    printKPath(root, 51)
