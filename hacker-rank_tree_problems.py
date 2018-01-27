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


#https://www.hackerrank.com/challenges/tree-inorder-traversal/problem
"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def inOrder(root):
    if root.left:
        inOrder(root.left)
    print root.data,
    if root.right:
        inOrder(root.right)

#https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
mheight = 0
current_height = 0
def height(root):
    global mheight
    global current_height
    if not root.left and not root.right:
        if current_height > mheight:
            mheight = current_height
            current_height = current_height - 1
    else:
        current_height += 1
    if root.left:
        height(root.left)
    if root.right:
        height(root.right)
    return mheight
    