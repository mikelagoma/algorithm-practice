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

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://leetcode.com/problems/average-of-levels-in-binary-tree/description/
class Solution10:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        result = [[]]
        queue = []
        queue.append(root)
        queue.append(None)
        while(len(queue) > 0):
            node = queue.pop(0)
            if node == None:
                if len(queue) == 0:
                    break
                queue.append(None)
                result.append([])
                continue
            print(node.val)
            result[-1].append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return [sum(l)/len(l) for l in result]

# https://leetcode.com/problems/single-number/description/
class Solution11:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        is_new = True
        if not nums:
            return
        nums.sort()
        for idx, val in enumerate(nums):
            if idx == len(nums) - 1:
                return val
            if is_new and (val != nums[idx+1]):
                return val
            is_new = not is_new

# https://leetcode.com/problems/palindromic-substrings/description/
class Solution12:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(set(list(s))) == 1:
            return sum([i for i in range(len(s)+1)])
        count = 0
        for l_idx, l_l in enumerate(s):
            for r_idx, r_l in reversed(list(enumerate(s))):
                if r_idx <= l_idx:
                    break
                if l_l == r_l:
                    if self.is_palindrome(s[l_idx:r_idx+1]):
                        count += 1
        return count + len(s)

    def is_palindrome(self, s):
        for idx in range(0, len(s) // 2):
            if s[idx] != s[len(s) - 1 - idx]:
                return False
        return True

# https://leetcode.com/problems/find-pivot-index/description/
class Solution13:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_nums = sum(nums)
        left_sum = 0
        if sum(nums[1:]) == 0:
            return 0
        for idx, val in enumerate(nums[1:], start=1):
            left_sum += nums[idx-1]
            right_sum = sum_nums - left_sum - val
            if left_sum == right_sum:
                return idx
        return -1

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# ehttps://leetcode.com/problems/swap-nodes-in-pairs/description/
class Solution14:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        node = head
        count = 0
        while node:
            count += 1
            if count > 4:
                break
            one = None
            two = None
            three = None
            print(node.val)
            if not node:
                return
            if node.next:
                if node.next.next:
                    three = node.next.next
                two = node.next
                node = two
            else:
                node = one
            if node:
                print("PRINTING LIST!!!")
                print(node.val)
                if node.next:
                    print(node.next.val)
                    if node.next.next:
                        print(node.next.next.val)
                        if node.next.next.next:
                            print(node.next.next.val)
            if one:
                if two:
                    print("have 2!")
                    if three:
                        print("have 3!")
                        node = three
                        two.next = three
                    else:
                        node = None
                    two.next = one
                else:
                    node = None
            else: 
                "no node"
                node = None
            if node == None:
                break
        return head

# https://leetcode.com/problems/reverse-linked-list/description/
class Solution15:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # def traverse(prev, curr):
        #     traverse.count +=1
        #     if traverse.count == 10:
        #         return
        #     if not curr.next:
        #         head = curr
        #         return
        #     curr.next = traverse(curr, curr.next)
        #     return prev
        # traverse.count = 0
        # head = traverse(head, head.next)
        if not head:
            return None
        curr_node = head
        prev_node = curr_node
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        head.next = None
        head = prev_node
        return head

# https://leetcode.com/problems/queue-reconstruction-by-height/description/
class Solution16:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        self.people = people
        i_from = 0
        while i_from < len(people) - 2:
            print(self.people)
            count = self.people[i_from][1]
            height = self.people[i_from][0]
            if count == 0 and i_from == 0:
                i_from += 1
            for i_to, val in enumerate(self.people):
                if i_to == i_from:
                    continue
                if val[0] >= height:
                    if count == 0:
                        print('swapping {} to {}'.format(i_from, i_to))
                        self.swap(i_from, i_to)
                    count = count - 1
            i_from += 1


    def swap(self, a, b):
        print(a, b)
        print(self.people[a])
        print(self.people[b])
        self.people[a], self.people[b] = self.people[b], self.people[a]

# https://leetcode.com/problems/move-zeroes/description/
class Solution17:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        idx = 0
        end = len(nums)
        while idx < end:
            if nums[idx] == 0:
                zero_idx = idx
                for idx in range(zero_idx, end):
                    if nums[idx] != 0:
                        self.swap(nums, zero_idx, idx)
                        idx = 0
                        break
            idx += 1
        return nums

    def swap(self, l, a, b):
        l[a], l[b] = l[b], l[a]


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
    # s9 = Solution9()
    # print(s9.islandPerimeter(
    #     # [[1],[0]]
    #         [[0,1,0,0],
    #          [1,1,1,0],
    #          [0,1,0,0],
    #          [1,1,0,0]]
    #      ))
    # s10 = Solution10()
    # print(s10.averageOfLevels(bt.TreeNode(4)))
    # s11 = Solution11()
    # print(s11.singleNumber([1, 2, 3, 1, 4, 2, 3]))
    # s12 = Solution12()
    # print(s12.is_palindrome("aba"))
    # print(s12.is_palindrome("abaa"))
    # print(s12.countSubstrings("abacacaaaccbbbb"))
    # print(s12.countSubstrings("aaa"))
    # s13 = Solution13()
    # print(s13.pivotIndex([-1, -1, -1, -1, -1, 0]))
    one = ListNode(1)
    two = ListNode(2)
    three = ListNode(3)
    four = ListNode(4)
    # five = ListNode(5)
    one.next = two
    two.next = three
    three.next = four
    four.next = None
    # four.next = five
    # five.next = None
    # # s14 = Solution14()
    # s15 = Solution15()
    # # head = s14.swapPairs(one)
    # head = s15.reverseList(one)
    # # head = s14.swapPairs([1])
    # print('Final answer:\n{}'.format(head.val))
    # if head.next:
    #     print(head.next.val)
    #     if head.next.next:
    #         print(head.next.next.val)
    #         if head.next.next.next:
    #             print(head.next.next.next.val)
    #             if head.next.next.next.next:
    #                 print(head.next.next.next.next.val)
    # s16 = Solution16()
    # print(s16.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))
    s17 = Solution17()
    print(s17.moveZeroes([0, 1, 0, 3, 12]))


if __name__ == '__main__':
    main()


