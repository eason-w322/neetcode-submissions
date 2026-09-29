
import heapq
class Twitter:

    def __init__(self):
        self.time = 0
        self.tweet = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append((-self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.following[userId]
        users.add(userId)
        queue = []
        for u in users:
            if self.tweet[u]:
                queue.extend(self.tweet[u])
        heapq.heapify(queue)
        results = []
        if not queue:
            return []
        for _ in range(10):
            inverse_time, tweet = heapq.heappop(queue)
            results.append(tweet)
            if not queue:
                return results
        return results
            
                
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)


        
