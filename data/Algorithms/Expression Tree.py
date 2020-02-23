class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isOperator(c):
    if (c == '+' or c == '-' or c == '*'
            or c == '/' or c == '^'):
        return True
    else:
        return False

def inorder(t):
    if t is not None:
        inorder(t.left)
        print(t.data, end=" ")
        inorder(t.right)

def constructTree(postfix):
    stack = []
    for char in postfix:
        if not isOperator(char):
            t = Node(char)
            stack.append(t)
        else:
            t = Node(char)
            t1 = stack.pop()
            t2 = stack.pop()
            t.right = t1
            t.left = t2
            stack.append(t)
    t = stack.pop()
    return t

def evaluateExpressionTree(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return int(root.data)
    left_sum = evaluateExpressionTree(root.left)
    right_sum = evaluateExpressionTree(root.right)
    if root.data == '+':
        return left_sum + right_sum
    elif root.data == '-':
        return left_sum - right_sum
    elif root.data == '*':
        return left_sum * right_sum
    else:
        return left_sum / right_sum

if __name__ == "__main__":
    postfix = "5 10 + 15 20 * 25 * -".split()
    tree = constructTree(postfix)
    print("Infix expression is")
    inorder(tree)
    print(f"\nValue: {evaluateExpressionTree(tree)}")
