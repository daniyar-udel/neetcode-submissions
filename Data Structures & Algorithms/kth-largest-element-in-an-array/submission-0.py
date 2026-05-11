class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        max_heap = list()
        for num in nums:
            heapq.heappush(max_heap, -num)

        i = 0
        while i < k:
            kth = heapq.heappop(max_heap)
            i += 1
        return -kth