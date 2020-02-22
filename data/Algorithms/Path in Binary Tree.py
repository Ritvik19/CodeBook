from BinaryTree import Node


def printPaths(root):
    path = []
    printPathsRec(root, path, 0)

def printPathsRec(root, path, pathLen):
    if root is None:
        return
    if(len(path) > pathLen):
        path[pathLen] = root.data
    else:
        path.append(root.data)
    pathLen = pathLen + 1
    if root.left is None and root.right is None:
        print(*path)
    else:
        printPathsRec(root.left, path, pathLen)
        printPathsRec(root.right, path, pathLen)

if __name__ == "__main__":
    root = Node(27)
    root.left = Node(14)
    root.right = Node(35)
    root.left.left = Node(10)
    root.left.right = Node(19)
    root.right.left = Node(31)
    root.right.right = Node(42)
    print("Inorder:")
    print(*root.inorderTraversal(root))
    printPaths(root)
