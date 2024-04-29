from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        zero_binary = ['0' for _ in range(n)]
        nums_size = pow(2, n)
        nums_set = {0}
        nums = []

        def solve(binary: List[str], tmp_list: List[int]) -> None:
            if len(tmp_list) == nums_size:
                num = int(''.join(binary), 2)
                if num & (num-1) != 0:
                    return
                nonlocal nums
                nums = tmp_list.copy()
            for i in range(len(binary)-1, -1, -1):
                if len(nums) == nums_size:
                    return
                binary[i] = '0' if binary[i] != '0' else '1'
                num = int(''.join(binary), 2)
                if num not in nums_set:
                    nums_set.add(num)
                    tmp_list.append(num)
                    solve(binary, tmp_list)
                    nums_set.remove(num)
                    tmp_list.pop()
                binary[i] = '0' if binary[i] != '0' else '1'

        solve(zero_binary, [0])
        return list(nums)


solution = Solution()
n = 2
assert solution.grayCode(n) == [0,1,3,2]
