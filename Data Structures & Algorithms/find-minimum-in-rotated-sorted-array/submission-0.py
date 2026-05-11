class Solution:
    def findMin(self, nums: list[int]) -> int:

        l = 0 
        r = len(nums) - 1
        res = nums[0]

        while l <= r:
            if nums[l] <= nums[r]:
                return min(res, nums[l])
            
            mid = (l + r) // 2
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
            res = min(res, nums[mid])

        return res