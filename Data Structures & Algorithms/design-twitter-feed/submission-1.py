
import heapq
class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-(self.time), tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.following[userId]
        users.add(userId)

        candidates = []
        outputFeed = []
        for u in users:
            if self.tweets[u]:
                candidates.extend(self.tweets[u])
        heapq.heapify(candidates)
        
        for _ in range(10):
            if not candidates:
                return outputFeed
            feed = heapq.heappop(candidates)
            outputFeed.append(feed[1])
        return outputFeed



                
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)


        
