class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif c == ')' or c == ']' or c == '}':
                
                if not stack:
                    return False
                
                if stack[-1] == '(':
                    if c == ')':
                        stack.pop()
                    else:
                        return False
                
                elif stack[-1] == '[':
                    if c == ']':
                        stack.pop()
                    else:
                        return False
                
                elif stack[-1] == '{':
                    if c == '}':
                        stack.pop()
                    else:
                        return False
                                
        if stack:
            return False

        return True
        