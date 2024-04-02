from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals)
        merge_intervals = [sorted_intervals[0]]
        for interval in sorted_intervals[1:]:
            if interval[0] <= merge_intervals[-1][1] and interval[1] >= merge_intervals[-1][1]:
                merge_intervals[-1][1] = interval[1]
            elif interval[0] > merge_intervals[-1][1]:
                merge_intervals.append(interval)
        return merge_intervals


s = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(s.merge(intervals))
intervals = [[1,4],[4,5]]
print(s.merge(intervals))
intervals = [[]]
print(s.merge(intervals))
intervals = [[1,2],[4,5]]
print(s.merge(intervals))
intervals = [[4, 5], [1, 4]]
print(s.merge(intervals))
intervals = [[1, 4], [1, 4]]
print(s.merge(intervals))
intervals = [[1,4],[2,3]]
print(s.merge(intervals))
