class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        
        min_heap = list()
        for key, val in hashmap.items():
            heapq.heappush(min_heap, (val, key))

        for i in range(len(min_heap) - k):
            heapq.heappop(min_heap)
        
        return [key for _, key in min_heap]
            