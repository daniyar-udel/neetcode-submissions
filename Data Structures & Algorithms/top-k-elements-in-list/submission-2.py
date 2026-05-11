class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        hashmap = {}

        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
    
        sorted_hashmap = sorted(hashmap.items(), 
                                     key = lambda item: item[1],
                                     reverse=True)
        
        
        while len(sorted_hashmap) > k:
            sorted_hashmap.pop()
        
        return [_ for _, ind in sorted_hashmap]