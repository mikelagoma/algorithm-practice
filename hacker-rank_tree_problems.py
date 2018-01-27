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

#https://www.hackerrank.com/challenges/tree-top-view/problem
"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

switch_directions = False
def topView(root):
    global switch_directions
    print root.data,
    if not root.left:
        switch_directions = True
    if not switch_directions:
        topView(root.left)
    else:
        topView(root.right)

# https://www.hackerrank.com/challenges/tree-level-order-traversal/problem
"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def levelOrder(root):
    queue = list()
    queue.append(root)
    while len(queue) > 0:
        root = queue.pop(0)
        print root.data,
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def levelOrder(root):
    queue = list()
    queue.append(root)
    def traverse(queue):
        if len(queue) <= 0:
            return
        root = queue.pop(0)
        print root.data,
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)
        traverse(queue)
    traverse(queue)

# https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem
"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

def insert(r,val):
    if val < r.data:
        if not r.left:
            r.left = Node(val)
            return
        insert(r.left,val)
    if val > r.data:
        if not r.right:
            r.right = Node(val)
            return
        insert(r.right,val)
    return r