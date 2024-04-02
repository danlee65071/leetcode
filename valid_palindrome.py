class Solution:
    def isPalindrome(self, s: str) -> bool:
        clear_str = ''.join([c.lower() for c in s if c.isalpha() or c.isdigit()])
        left = 0
        right = len(clear_str) - 1
        while right > left:
            if clear_str[right] != clear_str[left]:
                return False
            right -= 1
            left += 1
        return True


s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a car"))
print(s.isPalindrome(" "))
print(s.isPalindrome(""))
print(s.isPalindrome("0P"))
