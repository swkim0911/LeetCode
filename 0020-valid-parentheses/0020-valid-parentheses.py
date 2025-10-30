class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_pair = {"}": "{", ")": "(", "]": "["} # {닫힌 괄호: 열린 괄호} 쌍
        for bracket in s:
            if bracket not in bracket_pair.keys():  # 열린 괄호인 경우 스택에 push
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
# 문자열을 선형으로 탐색하면서 괄호쌍이 올바른지 확인하기 위해서 스택을 사용한다.
# 열린 괄호라면 스택에 저장하고 닫힌 괄호라면 주어진 valid 특성을 만족하려면 stack.peek()으 문자와 한 쌍을 이루어야 한다.
# 만약 쌍을 이루는 문자열이라면 pop해서 더이상 고려하지 않는다.
# 단 열린 괄호를 만났지만 스택이 비어있는 경우, 혹은 로직이 끝났음에도 stack에 남은 문자가 있다면 이는 주어진 valid 특성을 만족하지 못하는 경우이다.
