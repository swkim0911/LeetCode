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
# 인풋으로 주어진 strs 배열의 첫번째 문자를 기준으로 나머지 strs 배열의 문자열들을 비교해서 가장 긴 접두사를 찾겠습니다.
# 그러기 전에 인풋 문자열 중에 가장 짧은 문자열의 길이를 찾아서, 이 길이만큼만 공통 문자열을 찾게하고, 첫번째 문자열의 (0 ~ len(first_str)) 위치의 문자와 첫번째 문자열 이후 문자열들의 동일 위치에서 같은지 비교하고 같으면 정답 문자열에 추가하고 다르면 그 즉시 break해서 최대 길이의 공통 접두사를 찾겠습니다.