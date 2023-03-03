class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for index, char in enumerate(s):
            # 문자가 이미 등장했고 윈도우 안에 그 문자가 있으면(이미 등장했어도 현재 윈도우 안에 없을 수도 있다. 이 경우, 윈도우에는 없으므로 윈도우에 추가해도 된다.)
            if char in used and start <= used[char]:
                start = used[char] + 1
            else: # 최대 부분 문자열 길이 갱신
                max_length = max(max_length, index - start + 1)
            
            # 현재 문자의 위치 삽입(문자가 이미 등장은 했어도 갱신을 해서 현재 윈도우에 있는 char의 index를 알아야 위에 if문이 제대로 동작한다)
            used[char] = index
        
        return max_length