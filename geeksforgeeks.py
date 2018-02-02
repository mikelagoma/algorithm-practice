# https://practice.geeksforgeeks.org/problems/level-order-traversal/1
'''Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function would be added by GfG's Online Judge.'''


"""
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
"""
# Your task is to complete this function
# Function should print the level order of the tree in required format
# only input to function is the root of the tree
def traverse_level_order( root ):
    # Code here
    def traverse(queue):
        root = queue.pop(0)
        if not root:
            return
        print(root.data)
        queue.append(root.left)
        queue.append(root.right)
        traverse(queue)
    traverse.level = 0
    queue = [root]
    traverse(queue)