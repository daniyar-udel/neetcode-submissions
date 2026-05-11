class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        max_heap = list()

        for stone in stones:
            heapq.heappush(max_heap, -stone)

        while len(max_heap) > 1:
            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)

            if x == y:
                continue
            if x < y:
                heapq.heappush(max_heap, -(y - x))
        
        if max_heap:
            return -max_heap[0]
        return 0