class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = list()

        for i in s:
            if i in ('(', '{', '['):
                stack.append(i)
            else:
                if not stack:
                    return False
                elem = stack.pop()
                if elem == '(' and i == ')':
                    continue
                elif elem == '{' and i == '}':
                    continue
                elif elem == '[' and i == ']':
                    continue
                else:
                    return False
        
        if stack:
            return False
        return True