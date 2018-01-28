#!/usr/bin/python

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

def main():
    s = Solution2()
    # print(s.letterCombinations('23'))
    print(s.lastRemaining(5034))

if __name__ == '__main__':
    main()