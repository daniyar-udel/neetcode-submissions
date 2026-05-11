class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lst = list()

        for num in nums:
            if num in lst:
                return True
            lst.append(num)
    
        return False   