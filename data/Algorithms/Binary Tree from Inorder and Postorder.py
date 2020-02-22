from BinaryTree import Node


def buildUtil(In, post, inStrt, inEnd, pIndex):
    if inStrt > inEnd:
        return None

    node = Node(post[pIndex[0]])
    pIndex[0] -= 1
    
    if inStrt == inEnd:
        return node

    iIndex = search(In, inStrt, inEnd, node.data)
    node.right = buildUtil(In, post, iIndex + 1, inEnd, pIndex)
    node.left = buildUtil(In, post, inStrt, iIndex - 1, pIndex)

    return node

def buildTree(In, post, n):
    pIndex = [n - 1]
    return buildUtil(In, post, 0, n - 1, pIndex)

def search(arr, strt, end, value):
    i = 0
    for i in range(strt, end + 1):
        if (arr[i] == value):
            break
    return i

if __name__ == '__main__':
    In = [4, 8, 2, 5, 1, 6, 3, 7]
    post = [8, 4, 5, 2, 6, 7, 3, 1]
    n = len(In)
    root = buildTree(In, post, n)
    print("Preorder of the constructed tree :")
    print(*root.preorderTraversal(root))
