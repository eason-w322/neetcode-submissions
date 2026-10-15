
import heapq
class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweet = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append((-self.time, tweetId))
        self.time += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        users = (self.following[userId]).copy()
        users.add(userId)
        max_heap = []
        for user in users:
            max_heap.extend(self.tweet[user])
        heapq.heapify(max_heap)
        results = []
        if not max_heap:
            return []
        for _ in range(10):
            time, tweetId = heapq.heappop(max_heap)
            results.append(tweetId)
            if not max_heap:
                break
        return results
                      
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)



        
