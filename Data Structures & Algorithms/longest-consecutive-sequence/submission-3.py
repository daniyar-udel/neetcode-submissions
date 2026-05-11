class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        if not nums:
            return 0

        nums = list(sorted(set(nums)))

        result = 1
        max_result = 1

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                result += 1
                max_result = max(max_result, result)
            else:
                result = 1

        return max_result
