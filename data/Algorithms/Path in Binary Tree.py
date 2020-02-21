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
    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)
    root.insert(45)
    print("Inorder:")
    print(*root.inorderTraversal(root))
    printPaths(root)
