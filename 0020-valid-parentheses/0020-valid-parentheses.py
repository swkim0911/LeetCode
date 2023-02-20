class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if stack:
                top = stack[-1]
                if top == "{":
                    if bracket == "}":
                        stack.pop()
                    else:
                        stack.append(bracket)
                elif top == "(":
                    if bracket == ")":
                        stack.pop()
                    else:
                        stack.append(bracket)
                if top == "[":
                    if bracket == "]":
                        stack.pop()
                    else:
                        stack.append(bracket)
                continue

            stack.append(bracket)

        if len(stack) == 0:
            return True
        else:
            return False