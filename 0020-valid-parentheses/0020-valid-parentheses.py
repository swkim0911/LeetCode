class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_pair = {"}": "{", ")": "(", "]": "["}

        for bracket in s:
            if bracket == "(" or bracket == "{" or bracket == "[": # 열린 괄호인 경우 스택에 push
                stack.append(bracket)
            else: # 단힌 괄호인 경우
                if not stack: # 스택이 비어있는 경우
                    return False
                if stack[-1] == bracket_pair[bracket]:
                    stack.pop()
                else:
                    return False
        
        if stack:
            return False
        
        return True
            

# 문제는 주어진 문자열에 대해 괄호쌍이 올바른지 아닌지 확인하는 문제
# 문자열을 선형으로 탐색하면서 괄호쌍이 올바른지 확인하기 위해서 스택을 사용
