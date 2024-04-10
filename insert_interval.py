from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_intervals = []
        pos = 0
        while pos < len(intervals) and newInterval[0] > intervals[pos][1]:
            new_intervals.append(intervals[pos])
            pos += 1
        tmp_interval = newInterval
        while pos < len(intervals) and tmp_interval[1] >= intervals[pos][0] :
            tmp_interval[0] = min(tmp_interval[0], intervals[pos][0])
            tmp_interval[1] = max(tmp_interval[1], intervals[pos][1])
            pos += 1
        new_intervals.append(tmp_interval)
        while pos < len(intervals):
            new_intervals.append(intervals[pos])
            pos += 1
        return new_intervals


solution = Solution()
intervals = [[1,3],[6,9]]
newInterval = [2,5]
assert solution.insert(intervals, newInterval) == [[1,5],[6,9]]
intervals = [[4,5],[6,9]]
newInterval = [1,2]
assert solution.insert(intervals, newInterval) == [[1,2],[4,5],[6,9]]
intervals = [[2,5],[6,9]]
newInterval = [1,3]
assert solution.insert(intervals, newInterval) == [[1,5],[6,9]]
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
assert solution.insert(intervals, newInterval) == [[1,2],[3,10],[12,16]]
intervals = []
newInterval = [4,8]
assert solution.insert(intervals, newInterval) == [[4,8]]
intervals = [[1,5]]
newInterval = [6,8]
assert solution.insert(intervals, newInterval) == [[1,5],[6,8]]
