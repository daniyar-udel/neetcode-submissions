class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        lst = list()

        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1

            while l < r:
                summa = nums[i] + nums[l] + nums[r]
                if summa < 0:
                    l += 1
                elif summa > 0:
                    r -= 1
                else:
                    lst.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

        return lst
