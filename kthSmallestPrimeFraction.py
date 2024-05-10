from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        left, right = 0, 1
        while left < right:
            mid = (left + right) / 2
            total_smaller_fractions, max_fraction = 0, 0
            j = 1
            for i in range(len(arr) - 1):
                while j < len(arr) and arr[i] >= arr[j] * mid:
                    j += 1
                total_smaller_fractions += len(arr) - j
                if j >= len(arr):
                    break
                fraction = arr[i] / arr[j]
                if fraction > max_fraction:
                    numerator_idx = i
                    denumerator_idx = j
                    max_fraction = fraction
            if total_smaller_fractions == k:
                return [arr[numerator_idx], arr[denumerator_idx]]
            elif total_smaller_fractions < k:
                left = mid
            else:
                right = mid
        return []
