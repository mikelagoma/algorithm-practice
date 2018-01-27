# https://www.hackerrank.com/challenges/tree-preorder-traversal/problem
"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def preOrder(root):
    print root.data,
    if root.left:
        preOrder(root.left)
    if root.right:
        preOrder(root.right)

# https://www.hackerrank.com/challenges/tree-postorder-traversal/problem
"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def postOrder(root):
    if root.left:
        postOrder(root.left)
    if root.right:
        postOrder(root.right)
    print root.data,

