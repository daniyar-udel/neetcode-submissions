class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        
        l = 0
        r = len(numbers) - 1

        while l <= r:
            summa = numbers[l] + numbers[r]
            if summa == target:
                return [l + 1, r + 1]
            elif summa < target:
                l += 1
            else:
                r -= 1
        
        return []