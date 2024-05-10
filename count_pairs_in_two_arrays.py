from typing import List


class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        sorted_diff = sorted([n1 - n2 for n1, n2 in zip(nums1, nums2)])
        res = 0
        for i in range(len(sorted_diff)):
            if sorted_diff[i] > 0:
                res += len(sorted_diff) - i - 1
            else:
                l, r = i + 1, len(sorted_diff) - 1
                m = (l + r) // 2
                while l <= r:
                    if sorted_diff[i] + sorted_diff[m] > 0:
                        r = m - 1
                    else:
                        l = m + 1
                res += len(sorted_diff) - l
        return res
