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
                diff = y - x
                heapq.heappush(max_heap, -diff)
        
        if not max_heap:
            return 0
        
        return -max_heap[0]
