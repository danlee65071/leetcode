class Solution:
    def simplifyPath(self, path: str) -> str:
        list_dirs = path.split('/')
        stack = []
        for el in list_dirs:
            if el == '..':
                if stack:
                    stack.pop()
            elif el == '.' or not el:
                continue
            else:
                stack.append(el)
        return '/' + '/'.join(stack)


solution = Solution()
path = "/home/"
assert solution.simplifyPath(path) == '/home'
path = "/../"
assert solution.simplifyPath(path) == '/'
path = "/home//foo/"
assert solution.simplifyPath(path) == '/home/foo'
