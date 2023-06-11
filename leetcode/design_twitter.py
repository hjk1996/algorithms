# tag: heap, design
# description
'''
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

Twitter() Initializes your twitter object.

void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. 
Each call to this function will be made with a unique tweetId.

List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. 
Each item in the news feed must be posted by users who the user followed or by the user themself. 
Tweets must be ordered from most recent to least recent.

void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.

void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
'''


from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        # count is used to keep track of the order of tweets
        self.count = 0
        # tweetMap is a map from userId to a list of tuples (count, tweetId)
        self.tweetMap = defaultdict(list)
        # followMap is a map from userId to a set of followeeIds
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.count, tweetId))
        self.count -= 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        followeeIds = self.followMap[userId]
        # add userId to followeeIds so that we can get user tweets as well
        followeeIds.add(userId)

        for followeeId in followeeIds:
            # get tweets from each followeeId
            tweets = self.tweetMap[followeeId]
            # if tweets is not empty, add the last tweet to minHeap
            if tweets:
                index = len(tweets)-1
                count, tweetId = tweets[index]
                # add (count, tweetId, followeeId, index) to minHeap
                # count is used to sort tweets in minHeap
                # followeeId is used to keep track of which followeeId the tweet is from
                # index is used to keep track of the index of the tweet in the tweets list
                minHeap.append((count, tweetId, followeeId, index-1))
        
        heapq.heapify(minHeap)

        # get the 10 most recent tweets from minHeap
        while minHeap and len(res) < 10:
            # get the tweet with the smallest count
            count, tweetId, followeeId, nextIndex = heapq.heappop(minHeap)
            # add tweetId to res
            res.append(tweetId)

            # if nextIndex >= 0, there are more tweets from the followeeId
            if nextIndex >= 0:
                # get the next tweet from the followeeId
                count, tweetId = self.tweetMap[followeeId][nextIndex]
                # add (count, tweetId, followeeId, nextIndex) to minHeap
                heapq.heappush(minHeap, (count, tweetId, followeeId, nextIndex-1))

        return res     



    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        

