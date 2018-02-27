#!/usr/bin/python3

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


# https://practice.geeksforgeeks.org/problems/does-robot-moves-circular/0
def is_circular(path):
    direction_map = {
        0 : 'North',
        1 : 'East',
        2 : 'South',
        3 : 'West',
    }
    x = 0
    y = 0
    direction = 0
    for action in list(path):
        if action == 'G':
            if direction == 0:
                y += 1
            if direction == 1:
                x += 1
            if direction == 2:
                y = y - 1
            if direction == 3:
                x = x - 1
        if action == 'L':
            if direction == 0:
                direction = 3
            else:
                direction = direction - 1
        if action == 'R':
            if direction == 3:
                direction = 0
            else:
                direction += 1
    if x == 0 and y == 0:
        answer = 'Circular'
    else:
        answer = 'Not Circular'
    return answer

def main():
    path = "GLGLGLG"
    print(is_circular(path))
    path = "GLLG"
    print(is_circular(path))
    path = "GGGG"
    print(is_circular(path))
    path = "GRGRGRG"
    print(is_circular(path))
    path = "GLRLGRLLGLRLG"
    print(is_circular(path))
    # N = int(input())
    # for i in range(N):
    #     print(input())
    return

if __name__ == '__main__':
    main()
