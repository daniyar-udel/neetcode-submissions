class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        max_heap = list()
        for x, y in points:
            dist = x * x + y * y
            heapq.heappush(max_heap, (-dist, (x, y)))
            while len(max_heap) > k:
                heapq.heappop(max_heap)
        return [p for _, p in max_heap]