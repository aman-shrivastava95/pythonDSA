from typing import Optional


class Node:
    def __init__(self, data: int):
        self.data :int = data
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None


def inorder(node:Optional["Node"]):
    if node:
        inorder(node.left)
        print(node.data,end=' ')
        inorder(node.right)

def preorder(node: Optional["Node"]):
    if node:
        print(node.data,end=' ')
        preorder(node.left)
        preorder(node.right)

def postorder(node: Optional["Node"] ):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data,end=' ')



root = Node(1);
root.left = Node(2);
root.right = Node(3);
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

inorder(root)
print()
preorder(root)
print()
postorder(root)
