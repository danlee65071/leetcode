from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        sorted_people: List = sorted(people)
        num_boats: int = 0
        left: int = 0
        right: int = len(people) - 1
        while left <= right:
            if sorted_people[left] + sorted_people[right] <= limit:
                left += 1
            num_boats += 1
            right -= 1
        return num_boats


solution: Solution = Solution()
people = [1,2]
limit = 3
assert solution.numRescueBoats(people, limit) == 1
people = [3,2,2,1]
limit = 3
assert solution.numRescueBoats(people, limit) == 3
people = [3,5,3,4]
limit = 5
assert solution.numRescueBoats(people, limit) == 4
people = [5,1,4,2]
limit = 6
assert solution.numRescueBoats(people, limit) == 2
