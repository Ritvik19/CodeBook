from BinaryTree import Node


def zizagtraversal(root):
    if root is None:
        return
    currentLevel = []
    nextLevel = []
    ltr = True
    currentLevel.append(root)

    while len(currentLevel) > 0:
        temp = currentLevel.pop(-1)
        print(temp.data, " ", end="")

        if ltr:
            if temp.left:
                nextLevel.append(temp.left)
            if temp.right:
                nextLevel.append(temp.right)
        else:
            if temp.right:
                nextLevel.append(temp.right)
            if temp.left:
                nextLevel.append(temp.left)

        if len(currentLevel) == 0:
            ltr = not ltr
            currentLevel, nextLevel = nextLevel, currentLevel

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
    print("Zigzag Order traversal of binary tree is") 
    zizagtraversal(root)
