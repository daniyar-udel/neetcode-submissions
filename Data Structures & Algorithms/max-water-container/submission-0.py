class Solution:
    def maxArea(self, heights: list[int]) -> int:

        max_store = 0

        l = 0
        r = len(heights) - 1

        while l <= r:
            mini = min(heights[l], heights[r])
            store = mini * (r - l)
            max_store = max(max_store, store)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return max_store