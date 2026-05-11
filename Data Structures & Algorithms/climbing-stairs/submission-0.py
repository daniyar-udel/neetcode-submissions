class Solution:
    def climbStairs(self, n: int) -> int:
        
        lst = list()

        for i in range(n + 1):
            if i == 0:
                lst.append(1)
            elif i == 1:
                lst.append(1)
            else:
                lst.append(lst[i-1] + lst[i-2])
        
        return lst[-1]