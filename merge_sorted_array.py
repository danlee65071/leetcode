from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        it1, it2 = m-1, n-1
        while it1 >= 0 or it2 >= 0:
            if it1 >= 0 and it2 < 0:
                nums1[it2+it1+1] = nums1[it1]
                it1 -= 1
            elif it2 >= 0 and it1 < 0:
                nums1[it2+it1+1] = nums2[it2]
                it2 -= 1
            else:
                if nums1[it1] >= nums2[it2]:
                    nums1[it1+it2+1] = nums1[it1]
                    it1 -= 1
                else:
                    nums1[it1+it2+1] = nums2[it2]
                    it2 -= 1


solution = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
solution.merge(nums1, m, nums2, n)
assert nums1 == [1,2,2,3,5,6]
nums1 = [1]
m = 1
nums2 = []
n = 0
solution.merge(nums1, m, nums2, n)
assert nums1 == [1]
nums1 = [4,5,6,0,0,0]
m = 3
nums2 = [1,2,3]
n = 3
solution.merge(nums1, m, nums2, n)
assert nums1 == [1,2,3,4,5,6]
