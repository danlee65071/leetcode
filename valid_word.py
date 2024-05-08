class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        num_vowels, num_consonant = 0, 0
        set_vowels = {'a', 'e', 'i', 'o', 'u'}
        for c in word:
            if c.isdigit():
                continue
            elif c.lower() in set_vowels:
                num_vowels += 1
            elif c.isalpha():
                num_consonant += 1
            else:
                return False
        return True if num_vowels >= 1 and num_consonant >= 1 else False


solution = Solution()
word = "UuE6"
assert solution.isValid(word) == True
