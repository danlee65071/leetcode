from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        new_chars = []
        count_char = 1
        cur_char = chars[0]
        new_chars.append(cur_char)
        for char in chars[1:]:
            if cur_char == char:
                count_char += 1
            else:
                if count_char > 1:
                    new_chars += list(str(count_char))
                count_char = 1
                cur_char = char
                new_chars.append(cur_char)
        if count_char > 1:
            new_chars += list(str(count_char))
        chars[:] = new_chars
        return len(chars)


s = Solution()
chars = ["a","a","b","b","c","c","c"]
print(s.compress(chars))
print(chars)
chars = ["a"]
print(s.compress(chars))
print(chars)
