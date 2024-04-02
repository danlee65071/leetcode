from typing import List, Union


class Solution:
    def __init__(self):
        self.chain_pairs = []

    def choose_first_pair(self, pairs: List[List[int]]) -> List[int]:
        first_pair = pairs[0]
        for pair in pairs:
            if pair[1] < first_pair[1]:
                first_pair = pair
        return first_pair

    def chose_next_pair(self, pairs: List[List[int]]) -> Union[List[int], None]:
        temp_pairs = [pair for pair in pairs if pair not in self.chain_pairs]
        b = self.chain_pairs[-1][-1]
        next_pair = None
        for pair in temp_pairs:
            c = pair[0]
            if (c > b) and (next_pair is None or pair[1] < next_pair[1]):
                next_pair = pair
        return next_pair

    def findLongestChain(self, pairs: List[List[int]]) -> int:
        self.chain_pairs.append(self.choose_first_pair(pairs))
        next_pair = self.chose_next_pair(pairs)
        while next_pair is not None:
            self.chain_pairs.append(next_pair)
            next_pair = self.chose_next_pair(pairs)
        return len(self.chain_pairs)


tests = [
    [[1, 2], [7, 8], [4, 5]],
    [[1, 2], [2, 3], [3, 4]],
    [[7, 9], [4, 5], [7, 9], [-7, -1], [0, 10], [3, 10], [3, 6], [2, 3]]
]
for idx, test in enumerate(tests):
    s = Solution()
    print(f'Test: {idx}')
    print(f'\tInput: {test}')
    print(f'\tOutput: {s.findLongestChain(test)}')
