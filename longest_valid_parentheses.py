class Solution:
    # def longestValidParentheses(self, s: str) -> int:
    #     longest_parentheses = 0
    #     num_open, num_close = 0, 0
    #     for it in range(len(s)):
    #         if s[it] == '(':
    #             num_open += 1
    #         else:
    #             num_close += 1
    #         if num_open == num_close:
    #             longest_parentheses = max(longest_parentheses, 2 * num_open)
    #         elif num_close > num_open:
    #             num_open, num_close = 0, 0
    #     num_open, num_close = 0, 0
    #     for it in range(len(s) - 1, -1, -1):
    #         if s[it] == '(':
    #             num_open += 1
    #         else:
    #             num_close += 1
    #         if num_open == num_close:
    #             longest_parentheses = max(longest_parentheses, 2 * num_open)
    #         elif num_close < num_open:
    #             num_open, num_close = 0, 0
    #     return longest_parentheses
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        longest_p = 0
        for it, p in enumerate(s):
            if p == '(':
                stack.append(it)
            else:
                stack.pop()
                if not stack:
                    stack.append(it)
                else:
                    longest_p = max(longest_p, it - stack[-1])
        return longest_p


solution = Solution()
s = "(()"
print(solution.longestValidParentheses(s))
s = ")()())"
print(solution.longestValidParentheses(s))
s = "()(()"
print(solution.longestValidParentheses(s))
s = "(()()"
print(solution.longestValidParentheses(s))
