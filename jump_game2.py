from typing import List


class Solution:
    # def jump(self, nums: List[int]) -> int:
    #     jumps_dict = dict()
    #     min_jumps_count = len(nums)

    #     def next_jump(position, jump_val, jumps_count):
    #         if position == len(nums) - 1:
    #             nonlocal min_jumps_count
    #             min_jumps_count = min(min_jumps_count, jumps_count)
    #             return
    #         if jumps_dict.get(position) is None:
    #             for v in range(1, jump_val+1):
    #                 if position + v < len(nums):
    #                     next_jump(position + v, nums[position + v], jumps_count + 1)
    #                     if jumps_dict.get(position) is None or min_jumps_count - jumps_count < jumps_dict.get(position):
    #                         jumps_dict[position] = min_jumps_count - jumps_count
    #         else:
    #             jumps_count += jumps_dict[position]
    #             min_jumps_count = min(min_jumps_count, jumps_count)

    #     next_jump(0, nums[0], 0)
    #     return min_jumps_count
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        num_jumps, i = 0, 0
        coverage, prev_pos = 0, 0
        for i in range(len(nums)):
            coverage = max(coverage, i + nums[i])
            if i == prev_pos:
                prev_pos = coverage
                num_jumps += 1
                if coverage >= len(nums) - 1:
                    break
            i += 1
        return num_jumps


solution = Solution()
nums = [2,3,1,1,4]
assert solution.jump(nums) == 2
nums = [2,3,0,1,4]
assert solution.jump(nums) == 2
nums = [2,1]
assert solution.jump(nums) == 1
nums = [1,2,1,1,1]
assert solution.jump(nums) == 3
nums = [2,1,1,1,1]
assert solution.jump(nums) == 3
