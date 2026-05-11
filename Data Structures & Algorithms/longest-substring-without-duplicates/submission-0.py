class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        lst = list()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in lst:
                lst.remove(s[l])
                l += 1
            lst.append(s[r])
            res = max(res, r - l + 1)
        
        return res