import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        traversal = ''

        if root != None:
            queue = [root]
            while len(queue) != 0:
                traversal += str(queue[0].data) + ' '
                if queue[0].left != None:
                    queue.append(queue[0].left)
                if queue[0].right != None:
                    queue.append(queue[0].right)
                queue.pop(0)
        print(traversal)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
