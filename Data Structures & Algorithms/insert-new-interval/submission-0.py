class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        intervals = sorted(intervals, key = lambda val: val[0])
        output = [intervals[0]]

        for start, end in intervals:
            lastend = output[-1][1]
            if lastend >= start:
                output[-1][1] = max(lastend, end)
            else:
                output.append([start, end])

        return output