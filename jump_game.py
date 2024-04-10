from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        is_possible = False
        jump_positions = set()

        def solve(position: int) -> None:
            if position == len(nums) - 1:
                nonlocal is_possible
                is_possible = True
                return
            max_jump = nums[position]
            for jump_val in range(1, max_jump+1):
                if is_possible:
                    return
                if position + jump_val in jump_positions:
                    continue
                jump_positions.add(position + jump_val)
                solve(position+jump_val)

        solve(0)
        return is_possible


solution = Solution()
nums = [2,3,1,1,4]
assert solution.canJump(nums) == True
nums = [3,2,1,0,4]
assert solution.canJump(nums) == False
nums = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
assert solution.canJump(nums) == False
