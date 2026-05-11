class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        lst = list()

        for i in range(len(nums)):
            if i == 0:
                lst.append(nums[i])
            else:
                lst.append(max(nums[i], nums[i] + lst[i-1]))
        
        return max(lst)