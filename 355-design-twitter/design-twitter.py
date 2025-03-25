class Twitter(object):

    def __init__(self):
        self.Tweets = {}
        self.followers = {}
        self.count = 0

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.count += 1
        if userId in self.Tweets.keys():
            self.Tweets[userId].append((self.count,tweetId))
        else:
            self.Tweets[userId] = [(self.count,tweetId)]
        

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        maxHeap = []
        if userId in self.Tweets.keys():
            maxHeap.extend(self.Tweets[userId])

        if userId in self.followers.keys():
            for fl in self.followers[userId]:
                if fl in self.Tweets.keys():
                    maxHeap.extend(self.Tweets[fl])
        
        maxHeap = [(-cnt,twtId) for cnt,twtId in maxHeap]
        heapq.heapify(maxHeap)
        n = min(10,len(maxHeap))
        res = []
        for _ in range(n):
            cnt , twtId = heapq.heappop(maxHeap)
            res.append(twtId)
        return res


    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId == followeeId :
            return
        
        if followerId in self.followers.keys() :
            if followeeId not in self.followers[followerId]:
                self.followers[followerId].append(followeeId)
        else:
            self.followers[followerId] = [followeeId]

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId == followeeId:
            return
        if followerId in self.followers.keys() and followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)