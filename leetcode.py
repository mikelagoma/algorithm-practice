#!/usr/bin/python3
import binary_tree as bt
from collections import Counter

# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
class Solution1:
    digit_letter_map = {
        0 : [],
        1 : [],
        2 : ['a', 'b', 'c'],
        3 : ['d', 'e', 'f'],
        4 : ['g', 'h', 'i'],
        5 : ['j', 'k', 'l'],
        6 : ['m', 'n', 'o'],
        7 : ['p', 'q', 'r', 's'],
        8 : ['t', 'u', 'v'],
        9 : ['w', 'x', 'y', 'z']
    }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        buildup = list()
        digits = [int(d) for d in digits]
        for digit in digits:
            if not buildup:
                buildup = Solution.digit_letter_map[digit]
            else:
                new_buildup = list()
                for b in buildup:
                    new_buildup = [b + letter for letter in Solution.digit_letter_map[digit]]
                buildup = new_buildup
        return buildup


# https://leetcode.com/problems/design-twitter/description/
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        Args:
            newsFeed : [
                (userId, tweetId)
            ]
            following : {
                "userId" : ["userId1", "userId2"]
            }
        """
        self.newsFeed = list()
        self.following = dict()

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.newsFeed.append((userId, tweetId))

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        feed = list()
        print(feed)
        for tweet in list(reversed(self.newsFeed)):
            if userId in self.following:
                if (tweet[0] in self.following[userId]) or \
                    (tweet[0] is userId):
                    feed.append(tweet[1])
            elif tweet[0] is userId:
                feed.append(tweet[1])
            if len(feed) == 10:
                break
        return feed

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.following:
            if followeeId not in self.following[followerId]:
                self.following[followerId].append(followeeId)
        else:
            self.following[followerId] = [followeeId]
        

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.following:
            if followeeId in self.following[followerId]:
                self.following[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

# https://leetcode.com/problems/elimination-game/description/
class Solution2:
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        numbers = [i+1 for i in range(n)]
        start_from_left = True
        while len(numbers) > 1:
            print(numbers)
            keep = list()
            if not start_from_left:
                numbers = list(reversed(numbers))
            for idx, value in enumerate(numbers):
                if idx % 2 == 1:
                    keep.append(idx)
            numbers = [numbers[idx] for idx in keep]
            if not start_from_left:
                numbers = list(reversed(numbers))
            start_from_left = not start_from_left
        return numbers[0]

# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution3:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
         [-10,-3,0,5,9,10],
         [-10,-3,0,9,10],
         [-10,-3,5,9],
        """
        if not nums:
            return
        tree = [nums[len(nums) // 2]]
        del nums[len(nums) // 2]
        add_left = True
        while nums:
            print('tree: {}\nnums: {}'.format(tree, nums))
            middle = len(nums) // 2
            if add_left:
                add_idx = middle // 2
                tree.append(nums[add_idx])
                del nums[add_idx]
                add_left = not add_left
                continue
            add_idx = len(nums) - (middle // 2) - 1
            tree.append(nums[add_idx])
            del nums[add_idx]
            add_left = not add_left
        return self.array_to_tree(tree)

    def array_to_tree(self, tree):
        root = TreeNode(tree[0])
        for tn in tree[1:]:
            self.insert(root, tn)
        return root

    def insert(self, root, val):
        if val < root.val:
            if not root.left:
                root.left = TreeNode(val)
            else:
                self.insert(root.left, val)
        if val > root.val:
            if not root.right:
                root.right = TreeNode(val)
            else:
                self.insert(root.right, val)

# https://leetcode.com/problems/jewels-and-stones/description/
class Solution4:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        if not J or not S:
            return 0
        count = 0
        num_stones = {}
        for s in S:
            num_stones[s] = num_stones.get(s, 0) + 1
        for s in num_stones:
            if s in J:
                count += num_stones[s]
        return count

# https://leetcode.com/problems/maximum-binary-tree/description/
class Solution5:
    def constructMaximumBinaryTree(self, nums, root=None):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return
        print(max(nums))
        root = binary_tree.TreeNode(max(nums))
        max_idx = nums.index(root.val)
        root.left = self.constructMaximumBinaryTree(nums[:max_idx], root)
        root.right = self.constructMaximumBinaryTree(nums[max_idx+1:], root)
        return root

# https://leetcode.com/problems/partition-labels/description/
class Solution6:
    def partition_labels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        partitions = []
        for s in S:
            # print(partitions)
            print(s)
            break_out = False
            for i, p in enumerate(partitions):
                if s in p:
                    partitions = self.combine_prev_partitions(partitions, i)
                    print('got these: {}'.format(partitions))
                    partitions[i][s] = partitions[i][s] + 1
                    print('BREAKING')
                    break_out = True
                    break
            if break_out:
                break_out = False
                continue
            print('APPENDING {}'.format(s))
            partitions.append({s : 1})
        return [sum(p.values()) for p in partitions]

    def combine_prev_partitions(self, partitions, i):
        new_partitions = partitions[0:i]
        print('using these: {} through index {}'.format(new_partitions, i))
        # new_partition = {}
        # for p in partitions[i:]:
        #     new_partition = {**new_partition, **p}
        # print(new_partition)
        new_partition = dict(sum(
            (Counter(dict(x)) for x in partitions[i:]),
            Counter()
            ))
        new_partitions.append(new_partition)
        print('returning these: {}'.format(new_partitions))
        return new_partitions

# https://leetcode.com/problems/merge-two-binary-trees/description/
class Solution7:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:
            return
        root = bt.TreeNode(0)
        if t1:
            root = self.traverse(root, t1)
        print('at value {} before second tree'.format(root.val))
        if t2:
            root = self.traverse(root, t2)
        return root

    def traverse(self, root, t):
        if not t:
            return
        print(t.val)
        print(root.val)
        root.val = root.val + t.val
        print(root.val)
        if t.left:
            if not root.left:
                root.left = bt.TreeNode(0)
            self.traverse(root.left, t.left)
        if t.right:
            if not root.right:
                root.right = bt.TreeNode(0)
            self.traverse(root.right, t.right)
        return root

# https://leetcode.com/problems/trim-a-binary-search-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution8:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return
        print(root.val)
        if root.val == L:
            root.left = None
        elif root.val == R:
            root.right = None
        if root.val < L or root.val > R:
            if root.left:
                if root.right:
                    root.left.right = root.right
                root = root.left
            elif root.right:
                root = root.right
            else:
                return None
            self.trimBST(root, L, R)
        if root.left:
            if root.left.val < L:
                if root.left.left:
                    if root.left.right:
                        root.left.left.right = root.left.right
                    root.left = root.left.left
                elif root.left.right:
                    root.left = root.left.right
                else:
                    root.left = None
            
        if root.right:
            if root.right.val > R:
                if root.right.left:
                    if root.right.right:
                        root.right.left.right = root.right.right
                    root.right = root.right.left
                elif root.right.right:
                    root.right = root.right.right
                else:
                    root.right = None
        self.trimBST(root.left, L, R)
        self.trimBST(root.right, L, R)
        return root

# https://leetcode.com/problems/island-perimeter/description/
class Solution9:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        for o in range(len(grid)):
            for i in range(len(grid[o])):
                if grid[o][i] == 1:
                    if i == 0:
                        perimeter += 1
                    elif len(grid[o]) > 1:
                        if grid[o][i-1] == 0:
                            perimeter += 1
                    if i == len(grid[o])-1:
                        perimeter += 1
                    elif len(grid[o]) > 1:
                        if grid[o][i+1] == 0:
                            perimeter += 1
                    if o == 0:
                        perimeter += 1
                    elif len(grid) > 1:
                        if grid[o-1][i] == 0:
                            perimeter += 1
                    if o == len(grid)-1:
                        perimeter += 1
                    elif len(grid) > 1:
                        if grid[o+1][i] == 0:
                            perimeter += 1
        return perimeter

def main():
    # s1 = Solution1()
    # print(s1.letterCombinations('23'))
    # s2 = Solution2()
    # print(s2.lastRemaining(5034))
    # s3 = Solution3()
    # print(s3.sortedArrayToBST([-10,-3,0,5,9]))
    # s4 = Solution4()
    # print(s4.numJewelsInStones("aA", "aAAbbbb"))
    # s5 = Solution5()
    # s5.constructMaximumBinaryTree([3,2,1,6,0,5])
    # s6 = Solution6()
    # print(s6.partition_labels("ababcbacadefegdehijhklij"))
    # s7 = Solution7()
    # s7.mergeTrees(bt.TreeNode(4), bt.TreeNode(4))
    s9 = Solution9()
    print(s9.islandPerimeter(
        # [[1],[0]]
            [[0,1,0,0],
             [1,1,1,0],
             [0,1,0,0],
             [1,1,0,0]]
         ))

if __name__ == '__main__':
    main()

