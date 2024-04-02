class Solution:
    def isValid(self, s: str) -> bool:
        map_parentheses = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack_parentheses = list()
        for parenthes in s:
            if parenthes == '(' or parenthes == '[' or parenthes == '{':
                stack_parentheses.append(parenthes)
            elif parenthes == ')' or parenthes == ']' or parenthes == '}':
                if len(stack_parentheses) == 0:
                    return False
                if stack_parentheses[-1] == map_parentheses[parenthes]:
                    stack_parentheses.pop()
                else:
                    return False
        if len(stack_parentheses) == 0:
            return True
        return False


s = Solution()

print('Test 1')
s1 = '()'
print(s.isValid(s1))

print('Test 2')
s2 = '()[]{}'
print(s.isValid(s2))

print('Test 3')
s3 = '(]'
print(s.isValid(s3))

print('Test 4')
s1 = '([)]'
print(s.isValid(s1))

print('Test 5')
s1 = ']'
print(s.isValid(s1))

print('Test 6')
s1 = '(])'
print(s.isValid(s1))
