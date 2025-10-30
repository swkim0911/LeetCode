class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        min_len = min(map(len, strs))
        for i in range(min_len):
            first_char = strs[0][i] # 첫번째 문자열의 i번째 문자
            is_same = True
            for j in range(1, len(strs)):
                if first_char != strs[j][i]:
                    is_same = False
                    break
            if is_same:
                answer += first_char
            else:
                break
            
        return answer

# 주어진 문자열들의 가장 긴 공통 접두사(common prefix)를 찾는 문제
# 