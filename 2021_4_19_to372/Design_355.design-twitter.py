'''
Design a simplified version of Twitter where users can post tweets,
follow/unfollow another user and is able to see the 10 most recent tweets
 in the user's news feed. Your design should support the following methods:

postTweet(userId, tweetId): Compose a new tweet.
getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's
 news feed. Each item in the news feed must be posted by users who the user
  followed or by the user herself. Tweets must be ordered from most recent
  to least recent.
follow(followerId, followeeId): Follower follows a followee.
unfollow(followerId, followeeId): Follower unfollows a followee.
Example:

Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet
id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);
'''
#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#

# @lc code=start
import collections
import itertools
import heapq


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timer = itertools.count(step=-1)
        self.tweets = collections.defaultdict(collections.deque)
        self.followees = collections.defaultdict(set)
        # itertools.count(start, [step])

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets[userId].appendleft((next(self.timer), tweetId))
        # next()
        # print("postTweet", self.timer, self.tweets, self.followees)
        # deque.appendleft()

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed.
        Each item in the news feed must be posted by users who the user
        followed or by the user herself. Tweets must be ordered from most
        recent to least recent.
        """
        tweets = heapq.merge(
            *(self.tweets[u] for u in self.followees[userId] | {userId}))
        # print("getNews", self.timer, self.tweets, self.followees)
        return [t for _, t in itertools.islice(tweets, 10)]
        # heapq.merge(*iterables, key=None, reverse=False)
        # Merge multiple sorted inputs into a single sorted output

        # islice(iterable, start, stop, step): This iterator selectively
        # prints the values mentioned in
        # its iterable container passed as an argument.

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should
         be a no-op.
        """
        self.followees[followerId].add(followeeId)
        # set.add(elem)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it 
        should be a no-op.
        """
        self.followees[followerId].discard(followeeId)
        # set.discard(value)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end
