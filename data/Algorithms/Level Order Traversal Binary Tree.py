from BinaryTree import Node

def levelordertraversal(root):
    h = height(root)
    for i in range(1, h+1):
        printGivenLevel(root, i)

def printGivenLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root, end=" ")
    elif level > 1:
        printGivenLevel(root.left, level-1)
        printGivenLevel(root.right, level-1)

def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)
        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1

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
    print("Level Order traversal of binary tree is") 
    levelordertraversal(root)
