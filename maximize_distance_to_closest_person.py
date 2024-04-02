from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        map_ranges = dict()
        start_range = end_range = None
        max_range = cur_range = 0
        for i, seat in enumerate(seats):
            if seat == 1:
                if start_range is not None and end_range is not None:
                    if start_range == 0:
                        cur_range = (cur_range - 1) * 2 + 1
                    map_ranges[cur_range] = (start_range, end_range)
                if cur_range > max_range:
                    max_range = cur_range
                start_range = end_range = None
                cur_range = 0
            else:
                cur_range += 1
                if start_range is None:
                    start_range = i
                end_range = i
        if end_range == len(seats) - 1:
            cur_range = (cur_range - 1) * 2 + 1
        
        if cur_range > max_range:
            max_range = cur_range
            map_ranges[max_range] = (start_range, end_range)
        longest_range = map_ranges[max_range]
        if longest_range[0] == 0 or longest_range[-1] == len(seats) - 1:
            return longest_range[1] - longest_range[0] + 1
        return sum(longest_range) // 2 - longest_range[0] + 1


s = Solution()
seats = [1,0,0,0,1,0,1]
print(s.maxDistToClosest(seats))
seats = [1,0,0,0]
print(s.maxDistToClosest(seats))
seats = [0,0,0,1]
print(s.maxDistToClosest(seats))
seats = [0,1]
print(s.maxDistToClosest(seats))
seats = [1,1,0,0,0,1,0]
print(s.maxDistToClosest(seats))
seats = [0,1,1,1,0,0,1,0,0]
print(s.maxDistToClosest(seats))
seats = [1,0,0,1,0,0,0,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0]
print(s.maxDistToClosest(seats))