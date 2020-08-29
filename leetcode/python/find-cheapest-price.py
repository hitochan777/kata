import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        edges = [[] for _ in range(n)]
        for u, v, w in flights:
            edges[u].append((v, w))

        dist = [(0, src, K+1)]
        while dist:
            d, cur, k = heapq.heappop(dist)
            if cur == dst:
                return d

            if k > 0:
                for v, w in edges[cur]:
                    heapq.heappush(dist, (d + w, v, k - 1))  

        return -1
