class Solution:
    def rob(self, nums: List[int]) -> int:
        
        new_houses = [0]

        for num in nums:
            new_houses.append(num)
        
        lst = list()

        for i in range(len(new_houses)):
            if i == 0:
                lst.append(new_houses[i])
            elif i == 1:
                lst.append(new_houses[i])
            else:
                lst.append(max(lst[i-1], new_houses[i] + lst[i-2]))
        
        return max(lst)