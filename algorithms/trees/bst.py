from typing import Optional


class Node:
    def __init__(self, val:int):
        self.val= val
        self.left: Optional["Node"] = None 
        self.right: Optional["Node"] = None

def insert(node: Optional["Node"], val) -> Node:
    if node is None:
        return Node(val)
    if val < node.val:
        node.left = insert(node.left, val)
    if val >= node.val:
        node.right = insert(node.right, val)

    return node


def inorder(node:Optional["Node"]):
    if node:
        inorder(node.left)
        print(node.val, end=' ')
        inorder(node.right)

r = Node(15)
r = insert(r, 10)
r = insert(r, 18)
r = insert(r, 4)
r = insert(r, 11)
r = insert(r, 16)
r = insert(r, 20)
r = insert(r, 13)

inorder(r)
