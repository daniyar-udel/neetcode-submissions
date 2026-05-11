class Solution:
    def isValid(self, s: str) -> bool:

        stack = list()

        for i in range(len(s)):
            if s[i] in ('(', '{', '['):
                stack.append(s[i])
            else:
                if not stack:
                    return False
                open_bracket = stack.pop()
                if open_bracket == '(' and s[i] == ')':
                    continue
                if open_bracket == '{' and s[i] == '}':
                    continue
                if open_bracket == '[' and s[i] == ']':
                    continue
                else:
                    return False
        
        if not stack:
            return True
        
        return False